using Grpc.Core;
using Reservation.Protos;
using Reservation.Persistency;

namespace Reservation.Services;

public class ReservationService : ReservationGrpc.ReservationGrpcBase
{
    private readonly ILogger<ReservationService> _logger;
    private readonly KafkaService _kafkaService;
    private readonly IReservationRepository _repository;

    public ReservationService(ILogger<ReservationService> logger, KafkaService kafkaService, IReservationRepository repository)
    {
        _logger = logger;
        _kafkaService = kafkaService;
        _repository = repository;
    }

    public override Task<ReservationResponse> CreateReservation(CreateReqeust request, ServerCallContext context)
    {
        ReservationResponse reservation = _repository.Create(request.ItemId, request.UserId);

        _kafkaService.ReservationCreatedEvent(reservation.ItemId);

        _logger.LogInformation("New reservation created: {reservation}", reservation);
        return Task.FromResult(reservation);
    }

    public override Task<RetriveResponse> RetriveUsersReservations(RetriveRequest request, ServerCallContext context)
    {
        IEnumerable<ReservationResponse> reservations = _repository.GetAll(request.UserId);
        RetriveResponse retriveResponse = new();
        retriveResponse.Reservations.AddRange(reservations);
        return Task.FromResult(retriveResponse);
    }
}
