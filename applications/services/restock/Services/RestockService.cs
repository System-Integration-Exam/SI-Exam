using Google.Protobuf.WellKnownTypes;
using Grpc.Core;
using Restock.Protos;

namespace Restock.Services;

public class RestockService : RestockGrpc.RestockGrpcBase
{
    private readonly ILogger<RestockService> _logger;
    public RestockService(ILogger<RestockService> logger)
    {
        _logger = logger;
    }

    public override Task<Empty> RequestRestock(RestockRequest request, ServerCallContext context)
    {
        return base.RequestRestock(request, context);
    }
}
