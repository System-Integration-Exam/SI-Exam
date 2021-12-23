using System.Net.Http.Headers;
using Camunda.Worker;
using Camunda.Worker.Client;
using Grpc.Net.Client;
using Metadata.Protos;
using Restock.Services;

var builder = WebApplication.CreateBuilder(args);

builder.Logging.ClearProviders();
builder.Logging.AddSimpleConsole();

string camundaBaseUrl = builder.Configuration.GetValue<string>("CamundaRestUrl");
Action<HttpClient> camunderHttpClientBuilder = client => client.BaseAddress = new Uri(camundaBaseUrl);

builder.Services.AddExternalTaskClient(camunderHttpClientBuilder);
builder.Services.AddCamundaWorker("dotnetWorker")
    .AddHandler<MetadataTaskHandler>();
builder.Services.AddScoped<MetadataClientService>();
builder.Services.AddScoped<CamundaDeploymentService>();

string metadataServiceUrl = builder.Configuration.GetValue<string>("MetadataServiceUrl");
builder.Services.AddScoped(services => new Book.BookClient(GrpcChannel.ForAddress(metadataServiceUrl)));
builder.Services.AddScoped(services => new Vinyl.VinylClient(GrpcChannel.ForAddress(metadataServiceUrl)));
builder.Services.AddScoped(services => new Song.SongClient(GrpcChannel.ForAddress(metadataServiceUrl)));

builder.Services.AddHttpClient("discogsVinylApi", client =>
{
    client.DefaultRequestHeaders.Authorization = new AuthenticationHeaderValue("Discogs", "key=BpRIWJrloHACjruiVMmi, secret=BzLPjQdcnXswOkyDTPyVMjdCUjWykuFi");
    client.DefaultRequestHeaders.UserAgent.Add(new ProductInfoHeaderValue("Mozilla", "5.0"));
});
builder.Services.AddHttpClient("camundaClient", camunderHttpClientBuilder);

// Add services to the container.
builder.Services.AddGrpc();

var app = builder.Build();

// Deploy Camunda files
using (IServiceScope scope = app.Services.CreateScope())
{
    CamundaDeploymentService deploymentService =  scope.ServiceProvider.GetService<CamundaDeploymentService>()!;
    await deploymentService.RemoveDefaultDeployments();
    await deploymentService.DeployRestockModelAsync();
}


// Configure the HTTP request pipeline.
app.MapGrpcService<RestockService>();
app.MapGet("/", () => "Communication with gRPC endpoints must be made through a gRPC client.");

app.Run();
