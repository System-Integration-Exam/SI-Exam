using System.Text.Json;
using System.Text.Json.Serialization;
using Confluent.Kafka;

namespace Reservation.Services;

public class KafkaService
{
    private readonly ProducerBuilder<string, string> _builder;
    private readonly string _topic;

    public KafkaService(IOptionsMonitor<AppSettings> options)
    {
        _topic = options.CurrentValue.KafkaReservationCreatedTopic;
        ProducerConfig config = new()
        {
            BootstrapServers = options.CurrentValue.KafkaBrokers
        };
        _builder = new ProducerBuilder<string, string>(config);
    }

    public void ReservationCreatedEvent(string itemId, int storeId, ReservationStatus status)
    {
        ReservationKafkaEvent reservation = new(itemId, storeId, status);
        using IProducer<string, string> producer = _builder.Build();

        Message<string, string> message = new()
        {
            Key = reservation.ItemId,
            Value = JsonSerializer.Serialize(reservation, new JsonSerializerOptions { Converters = { new JsonStringEnumConverter() } })
        };

        producer.Produce(_topic, message);
        producer.Flush();
    }

    private record ReservationKafkaEvent(string ItemId, int StoreId, ReservationStatus StatusCommand);
}
