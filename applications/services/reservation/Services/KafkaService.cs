using Confluent.Kafka;
using Microsoft.Extensions.Options;
using Reservation.Configuration;

namespace Reservation.Services;

public class KafkaService
{
    private readonly ProducerBuilder<Null, string> _builder;
    private readonly string _topic;

    public KafkaService(IOptionsMonitor<AppSettings> options)
    {
        _topic = options.CurrentValue.KafkaReservationCreatedTopic;
        ProducerConfig config = new()
        {
            BootstrapServers = options.CurrentValue.KafkaBrokers
        };
        _builder = new ProducerBuilder<Null, string>(config);
    }

    public void ReservationCreatedEvent(string bookId)
    {
        using IProducer<Null, string> producer = _builder.Build();

        Message<Null, string> message = new()
        {
            Value = bookId
        };

        producer.Produce(_topic, message);
        producer.Flush();
    }
}
