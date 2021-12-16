use crate::logic::kafka::reservation_message::ReservationMessage;
use crate::utils::config::{is_production_mode, CONFIG};

use log::{info, warn};

use rdkafka::client::ClientContext;
use rdkafka::config::{ClientConfig, RDKafkaLogLevel};
use rdkafka::consumer::stream_consumer::StreamConsumer;
use rdkafka::consumer::{CommitMode, Consumer, ConsumerContext, Rebalance};
use rdkafka::error::KafkaResult;
use rdkafka::message::Message;
use rdkafka::topic_partition_list::TopicPartitionList;

lazy_static! {
    static ref BOOTSTRAP_SERVERS: String = {
        if is_production_mode() {
            CONFIG.kafka.production.bootstrap_servers.clone()
        } else {
            CONFIG.kafka.development.bootstrap_servers.clone()
        }
    };
}

struct CustomContext;

impl ClientContext for CustomContext {}

impl ConsumerContext for CustomContext {
    fn pre_rebalance(&self, rebalance: &Rebalance) {
        info!("Pre rebalance {:?}", rebalance);
    }

    fn post_rebalance(&self, rebalance: &Rebalance) {
        info!("Post rebalance {:?}", rebalance);
    }

    fn commit_callback(&self, result: KafkaResult<()>, _offsets: &TopicPartitionList) {
        info!("Committing offsets: {:?}", result);
    }
}

// A type alias with your custom consumer can be created for convenience.
type LoggingConsumer = StreamConsumer<CustomContext>;

pub async fn consume_and_print(group_id: &str, topics: &[&str]) {
    let context = CustomContext;

    let consumer: LoggingConsumer = ClientConfig::new()
        .set("group.id", group_id)
        .set(
            "bootstrap.servers",
            BOOTSTRAP_SERVERS.to_owned(),
        )
        .set(
            "enable.partition.eof",
            CONFIG.kafka.consumer.enable_partition_eof.to_owned(),
        )
        .set(
            "session.timeout.ms",
            CONFIG.kafka.consumer.session_timeout_ms.to_owned(),
        )
        .set(
            "enable.auto.commit",
            CONFIG.kafka.consumer.enable_auto_commit.to_owned(),
        )
        //.set("statistics.interval.ms", "30000")
        //.set("auto.offset.reset", "smallest")
        .set_log_level(RDKafkaLogLevel::Debug)
        .create_with_context(context)
        .expect("Consumer creation failed");

    consumer
        .subscribe(&topics.to_vec())
        .expect("Can't subscribe to specified topics");

    loop {
        match consumer.recv().await {
            Err(e) => warn!("Kafka error: {}", e),
            Ok(m) => {
                match m.payload_view::<str>() {
                    None => (),
                    Some(Ok(s)) => ReservationMessage::from_payload(s.to_owned())
                        .and_resolve()
                        .await
                        .unwrap(),
                    Some(Err(e)) => {
                        warn!("Error while deserializing message payload: {:?}", e);
                        println!("Error happened on payload view: {}", e)
                    }
                };
                consumer.commit_message(&m, CommitMode::Async).unwrap();
            }
        };
    }
}
