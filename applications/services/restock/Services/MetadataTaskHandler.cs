using Camunda.Worker;
using Metadata.Protos;
using Restock.Models;

namespace Restock.Services;

[HandlerTopics("fetch-metadata")]
public class MetadataTaskHandler: IExternalTaskHandler
{
    private readonly ILogger<MetadataTaskHandler> _logger;
    private readonly IHttpClientFactory _clientFactory;
    private readonly MetadataClientService _metadataClient;

    public MetadataTaskHandler(ILogger<MetadataTaskHandler> logger, IHttpClientFactory clientFactoryFactory, MetadataClientService metadataClient)
    {
        _logger = logger;
        _clientFactory = clientFactoryFactory;
        _metadataClient = metadataClient;
    }

    public async Task<IExecutionResult> HandleAsync(ExternalTask externalTask, CancellationToken cancellationToken)
    {
        string itemType = externalTask.Variables["itemType"].Value?.ToString();
        
        _logger.LogInformation("Item type: {itemType}", itemType);

        CompleteResult result = new();
        result.Variables = externalTask.Variables;
        if (itemType == "book")
        {
            string isbn = externalTask.Variables["bookISBN"].Value?.ToString() 
                ?? throw new Exception("The variable 'bookISBN' from Camunda is empty");

            BookInfo info = await GetBookDataAsync(isbn);
            string itemId = await _metadataClient.AddBookAsync(info);
            result.Variables[nameof(itemId)] = Variable.String(itemId);
        }
        else if(itemType == "vinyl")
        {
            string artist = externalTask.Variables["vinylArtist"].Value?.ToString() 
                ?? throw new Exception("The variable 'vinylArtist' from Camunda is empty");
            string album = externalTask.Variables["vinylAlbum"].Value?.ToString() 
                ?? throw new Exception("The variable 'vinylAlbum' from Camunda is empty");

            VinylInfo info = await GetVinylDataAsync(artist, album);
            _logger.LogInformation(info.ToString());
        }
        
        return result;
    }

    private async Task<BookInfo> GetBookDataAsync(string isbn)
    {
        HttpClient client =  _clientFactory.CreateClient();
        VolumeList books = await client.GetFromJsonAsync<VolumeList>($"https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}") 
            ?? throw new Exception($"No books found with ISBN '{isbn}'");

        return books.Items.First().VolumeInfo;
    }

    private async Task<VinylInfo> GetVinylDataAsync(string artist, string album)
    {
        HttpClient client = _clientFactory.CreateClient("discogsVinylApi");
        SearchResults vinylSearch = await client.GetFromJsonAsync<SearchResults>($"https://api.discogs.com/database/search?artist={artist}&release_title={album}&type=release")
                                    ?? throw new Exception($"No vinyl found for artist '{artist}' with album title '{album}'");

        string masterUrl = vinylSearch.Results.First().MasterUrl;

        return await client.GetFromJsonAsync<VinylInfo>(masterUrl) 
            ?? throw new Exception($"Nothing found at '{masterUrl}'");
    }

    
}
