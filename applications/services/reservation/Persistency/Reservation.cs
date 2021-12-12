using System.ComponentModel.DataAnnotations.Schema;

namespace Reservation.Persistency;

public class Reservation
{
    public Guid Id { get; set; }
    public string ItemId { get; set; }
    public string UserId { get; set; }
    public DateTime CreatedAt { get; set; }
    public ReservationStatus Status { get; set; }

    public Reservation(string itemId, string userId)
    {
        ItemId = itemId;
        UserId = userId;
    }
}
