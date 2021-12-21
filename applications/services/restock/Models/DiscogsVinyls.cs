using System.Text.Json.Serialization;

namespace Restock.Models;

public class SearchResults
{
    public IEnumerable<SearchResult> Results { get; set; }
}

public class SearchResult
{
    [JsonPropertyName("master_url")]
    public string MasterUrl { get; set; }
}

public record VinylInfo
{
    public string Title { get; set; }
    public IEnumerable<VinylArtist> Artists { get; set; }
    [JsonPropertyName("tracklist")]
    public IEnumerable<VinylTrack> TrackList { get; set; }

    public IEnumerable<string> Genres { get; set; }
}

public record VinylArtist
{
    public string Name { get; set; }
}

public record VinylTrack
{
    public string Title { get; set; }
    public string Duration { get; set; }
}