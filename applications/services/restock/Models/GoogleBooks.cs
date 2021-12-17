namespace Restock.Models;

public class VolumeList
{
    public IEnumerable<Volume> Items { get; set; }
}
public class Volume
{
    public BookInfo VolumeInfo { get; set; }
}

public record BookInfo
{
    public IEnumerable<string> Authors { get; set; }
    public string Title { get; set; }
    public double AverageRating { get; set; }
}