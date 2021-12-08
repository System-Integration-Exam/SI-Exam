using Reservation.Configuration;
using Reservation.Services;

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddGrpc();
builder.Services.AddOptions<AppSettings>().BindConfiguration("AppSettings");
builder.Services.AddSingleton<KafkaService>();

var app = builder.Build();

// Configure the HTTP request pipeline.
app.MapGrpcService<ReservationService>();
app.MapGet("/", () => "Communication with gRPC endpoints must be made through a gRPC client. To learn how to create a client, visit: https://go.microsoft.com/fwlink/?linkid=2086909");

app.Run();
