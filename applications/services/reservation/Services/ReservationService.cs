using Google.Protobuf.WellKnownTypes;
using Grpc.Core;
using Reservation.Protos;

namespace Reservation.Services;

public class ReservationService : ReservationGrpc.ReservationGrpcBase
{
    private readonly ILogger<ReservationService> _logger;
    public ReservationService(ILogger<ReservationService> logger)
    {
        _logger = logger;
    }

    public override Task<Empty> CreateReservation(StringValue request, ServerCallContext context)
    {
        _logger.LogInformation($"Reservation created for: {request.Value}");
        return Task.FromResult(new Empty());
    }
}
