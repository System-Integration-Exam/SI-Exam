using Microsoft.EntityFrameworkCore;
using Reservation.Configuration;
using Reservation.Persistency;
using Reservation.Services;

var builder = WebApplication.CreateBuilder(args);

builder.Services.AddGrpc();
builder.Services.AddOptions<AppSettings>().BindConfiguration("AppSettings");
builder.Services.AddSingleton<KafkaService>();
builder.Services.AddScoped<IReservationRepository, ReservationRepository>();

string connString = builder.Configuration.GetConnectionString("ReservationContext");
builder.Services.AddDbContext<ReservationContext>(options => options.UseSqlite(connString));

var app = builder.Build();

// Configure the HTTP request pipeline.
app.MapGrpcService<ReservationService>();
app.MapGet("/", () => "Communication with gRPC endpoints must be made through a gRPC client. To learn how to create a client, visit: https://go.microsoft.com/fwlink/?linkid=2086909");

using (var scope = app.Services.CreateScope())
{
    var db = scope.ServiceProvider.GetRequiredService<ReservationContext>();
    db.Database.Migrate();
}

app.Run();
