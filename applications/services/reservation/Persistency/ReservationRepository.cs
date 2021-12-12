using Reservation.Protos;

namespace Reservation.Persistency;

public interface IReservationRepository
{
    IEnumerable<ReservationResponse> GetAll(string userId);
    ReservationResponse Create(string itemId, string userId);
    ReservationResponse UpdateStatus(string id, ReservationStatus status);
}

public class ReservationRepository: IReservationRepository
{
    private readonly ReservationContext _context;

    public ReservationRepository(ReservationContext context)
    {
        _context = context;
    }
    public IEnumerable<ReservationResponse> GetAll(string userId)
        => _context.Reservations
            .Where(x => x.UserId == userId)
            .Select(x => new ReservationResponse
            {
                Id = x.Id.ToString(), 
                ItemId = x.ItemId, 
                UserId = x.UserId,
                Status = (ReservationResponse.Types.Status)x.Status
            });

    public ReservationResponse Create(string itemId, string userId)
    {
        Reservation reservation = new(itemId, userId)
        {
            CreatedAt = DateTime.UtcNow,
            Status = ReservationStatus.Reserved
        };
        _context.Reservations.Add(reservation);
        _context.SaveChanges();

        return new()
        {
            Id = reservation.Id.ToString(),
            ItemId = reservation.ItemId,
            UserId = reservation.UserId,
            Status = (ReservationResponse.Types.Status)reservation.Status
        };
    }

    public ReservationResponse UpdateStatus(string id, ReservationStatus status)
    {
        Reservation reservation = _context.Reservations.First(x => x.Id.ToString() == id);
        if(reservation.Status == ReservationStatus.Reserved)
        {
            reservation.Status = status;
            _context.SaveChanges();
        }

        return new()
        {
            Id = reservation.Id.ToString(),
            ItemId = reservation.ItemId,
            UserId = reservation.UserId,
            Status = (ReservationResponse.Types.Status)reservation.Status
        };
    }
}
