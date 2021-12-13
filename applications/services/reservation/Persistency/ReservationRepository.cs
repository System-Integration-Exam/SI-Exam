using Reservation.Protos;

namespace Reservation.Persistency;

public interface IReservationRepository
{
    List<ReservationResponse> GetAll(string userId);
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
    public List<ReservationResponse> GetAll(string userId)
    {
        List<Reservation> reservations = _context.Reservations
            .Where(x => x.UserId == userId)
            .ToList();

        return reservations
            .Select(r => new ReservationResponse
            {
                Id = r.Id.ToString(), 
                ItemId = r.ItemId, 
                UserId = r.UserId, 
                Status = (ReservationResponse.Types.Status)r.Status
            }).ToList();
    }

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
        Guid requestId = Guid.Parse(id);
        Reservation reservation = _context.Reservations.First(x => x.Id == requestId);
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
