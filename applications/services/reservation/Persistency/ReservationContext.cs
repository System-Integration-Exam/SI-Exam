using Microsoft.EntityFrameworkCore;

namespace Reservation.Persistency;

public class ReservationContext: DbContext
{
    public DbSet<Reservation> Reservations => Set<Reservation>();


    public ReservationContext(DbContextOptions<ReservationContext> options): base(options) { }

    protected override void OnModelCreating(ModelBuilder modelBuilder)
    {
        modelBuilder.Entity<Reservation>(entity =>
        {
            entity.Property(r => r.ItemId)
                .IsRequired();
            entity.Property(r => r.UserId)
                .IsRequired();
            entity.Property(r => r.Status)
                .HasConversion<string>()
                .IsRequired();
            entity.Property(r => r.CreatedAt)
                .IsRequired();
        });
    }
}