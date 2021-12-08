namespace Reservation.Configuration;

public class AppSettings
{
    public string KafkaBrokers { get; set; } = "";
    public string KafkaReservationCreatedTopic { get; set; } = "";
}
