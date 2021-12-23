using Metadata.Protos;
using Restock.Models;

namespace Restock.Services;

public class MetadataClientService
{
    private readonly ILogger<MetadataClientService> _logger;
    private readonly Book.BookClient _bookClient;
    private readonly Vinyl.VinylClient _vinylClient;
    private readonly Song.SongClient _songClient;

    public MetadataClientService(ILogger<MetadataClientService> logger, Book.BookClient bookClient, Vinyl.VinylClient vinylClient, Song.SongClient songClient)
    {
        _logger = logger;
        _bookClient = bookClient;
        _vinylClient = vinylClient;
        _songClient = songClient;
    }

    public async Task<string> AddBookAsync(BookInfo bookInfo)
    {
        string authors = bookInfo.Authors.Aggregate((previous, current) => previous + "; " + current);
        CreateBookRequest bookRequest = new()
        {
            Title = bookInfo.Title, 
            Author = authors, 
            Rating = (int)bookInfo.AverageRating
        };
        _logger.LogInformation("Adding book to metadata service: {book}", bookRequest);
        CreateBookResponse response = await _bookClient.createBookAsync(bookRequest);

        return response.Book.Id;
    }

    public async Task<string> AddVinylAsync(VinylInfo vinylInfo)
    {
        string artists = vinylInfo.Artists.Select(x => x.Name).Aggregate((previous, current) => previous + "; " + current);
        string genres = vinylInfo.Genres.Aggregate((previous, current) => previous + "; " + current);
        CreateVinylRequest vinylRequest = new()
        {
            Artist = artists,
            Genre = genres
        };
        _logger.LogInformation("Adding vinyl to metadata service: {vinyl}", vinylRequest);
        CreateVinylResponse response = await _vinylClient.createVinylAsync(vinylRequest);

        string vinylId = response.Vinyl.Id;
        foreach (VinylTrack track in vinylInfo.TrackList)
        {
            CreateSongRequest songRequest = new()
            {
                Title=track.Title,
                DurationSec = (int)TimeSpan.Parse($"0:{track.Duration}").TotalSeconds,
                VinylId = vinylId
            };
            await _songClient.createSongAsync(songRequest);
        }
        return vinylId;
    }
}
