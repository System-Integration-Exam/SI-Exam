using System.Text.Json;
using System.Text.Json.Serialization;
using Google.Protobuf.WellKnownTypes;
using Grpc.Core;
using Restock.Models;
using Restock.Protos;

namespace Restock.Services;

public class RestockService : RestockGrpc.RestockGrpcBase
{
    private readonly ILogger<RestockService> _logger;
    private readonly HttpClient _httpClient;
    private readonly JsonSerializerOptions _jsonOptions;

    public RestockService(ILogger<RestockService> logger, IHttpClientFactory clientFactory)
    {
        _logger = logger;
        _httpClient = clientFactory.CreateClient("camundaClient");
        _jsonOptions = new()
        {
            Converters = { new JsonStringEnumConverter() }, 
            PropertyNamingPolicy = JsonNamingPolicy.CamelCase
        };
    }

    public override async Task<Empty> RequestRestock(RestockRequest request, ServerCallContext context)
    {
        var requestBody = new { 
            variables = new RequestVariables(
                request.ItemType.ToString().ToLower(),
                request.RequestText,
                request.ExistingItemCount,
                request.StoreId,
                request.ItemId
            )};

        await _httpClient.PostAsJsonAsync("process-definition/key/Restock_Process/submit-form", requestBody, _jsonOptions);
        _logger.LogInformation("{jsonBody}", JsonSerializer.Serialize(requestBody, _jsonOptions));
        return new Empty();
    }
}
