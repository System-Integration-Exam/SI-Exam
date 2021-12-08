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

    public override Task<Empty> CreateReservation(StringValue request, ServerCallContext context)
    {
        _kafkaService.ReservationCreatedEvent(request.Value);
        _logger.LogInformation($"Reservation created for: {request.Value}");
        return Task.FromResult(new Empty());
    }
}
