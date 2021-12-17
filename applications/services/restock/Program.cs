using Camunda.Worker;
using Camunda.Worker.Client;
using Grpc.Net.Client;
using Metadata.Protos;
using Restock.Services;

var builder = WebApplication.CreateBuilder(args);

string camundaBaseUrl = builder.Configuration.GetValue<string>("CamundaRestUrl");
Action<HttpClient> clientBuilder = client => client.BaseAddress = new Uri(camundaBaseUrl);

builder.Services.AddExternalTaskClient(clientBuilder);
builder.Services.AddCamundaWorker("dotnetWorker")
    .AddHandler<MetadataTaskHandler>();
builder.Services.AddHttpClient<RestockService>(clientBuilder);
builder.Services.AddSingleton<MetadataClientService>();

string bookServiceUrl = builder.Configuration.GetValue<string>("MetadataServiceUrl");
builder.Services.AddSingleton(services => new Book.BookClient(GrpcChannel.ForAddress(bookServiceUrl)));
builder.Services.AddHttpClient<MetadataTaskHandler>();

// Add services to the container.
builder.Services.AddGrpc();

var app = builder.Build();

// Configure the HTTP request pipeline.
app.MapGrpcService<RestockService>();
app.MapGet("/", () => "Communication with gRPC endpoints must be made through a gRPC client.");

app.Run();
