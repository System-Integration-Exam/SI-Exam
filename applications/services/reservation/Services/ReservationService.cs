using Google.Protobuf.WellKnownTypes;
using Grpc.Core;
using Reservation.Protos;

namespace Reservation.Services;

public class ReservationService : ReservationGrpc.ReservationGrpcBase
{
    private readonly ILogger<ReservationService> _logger;
    private readonly KafkaService _kafkaService;

    public ReservationService(ILogger<ReservationService> logger, KafkaService kafkaService)
    {
        _logger = logger;
        _kafkaService = kafkaService;
    }

    public override Task<ReservationResponse> CreateReservation(CreateReqeust request, ServerCallContext context)
    {
        _kafkaService.ReservationCreatedEvent(request.ItemId);
        _logger.LogInformation($"Reservation created for: {request.ItemId}");
        return Task.FromResult(new ReservationResponse());
    }
}
