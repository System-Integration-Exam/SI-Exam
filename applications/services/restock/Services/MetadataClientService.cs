using Metadata.Protos;
using Restock.Models;

namespace Restock.Services;

public class MetadataClientService
{
    private readonly ILogger<MetadataClientService> _logger;
    private readonly Book.BookClient _grpcClient;

    public MetadataClientService(ILogger<MetadataClientService> logger, Book.BookClient grpcClient)
    {
        _logger = logger;
        _grpcClient = grpcClient;
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
        CreateBookResponse response = await _grpcClient.createBookAsync(bookRequest);

        return response.Book.Id;
    }
}
