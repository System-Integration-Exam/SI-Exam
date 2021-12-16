using Camunda.Worker;
using Camunda.Worker.Client;
using Restock.Services;

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddExternalTaskClient(client => client.BaseAddress = new Uri("http://localhost:10000/engine-rest"));
builder.Services.AddCamundaWorker("dotnetWorker")
    .AddHandler<CamundaTaskHandler>();

// Add services to the container.
builder.Services.AddGrpc();

var app = builder.Build();

// Configure the HTTP request pipeline.
app.MapGrpcService<RestockService>();
app.MapGet("/", () => "Communication with gRPC endpoints must be made through a gRPC client.");

app.Run();
