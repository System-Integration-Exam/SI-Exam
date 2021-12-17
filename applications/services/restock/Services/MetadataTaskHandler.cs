using Camunda.Worker;
using Metadata.Protos;
using Restock.Models;

namespace Restock.Services;

[HandlerTopics("fetch-metadata")]
public class MetadataTaskHandler: IExternalTaskHandler
{
    private readonly ILogger<MetadataTaskHandler> _logger;
    private readonly HttpClient _httpClient;
    private readonly MetadataClientService _metadataClient;

    public MetadataTaskHandler(ILogger<MetadataTaskHandler> logger, HttpClient httpClient, MetadataClientService metadataClient)
    {
        _logger = logger;
        _httpClient = httpClient;
        _metadataClient = metadataClient;
    }

    public async Task<IExecutionResult> HandleAsync(ExternalTask externalTask, CancellationToken cancellationToken)
    {
        string isbn = externalTask.Variables["bookISBN"].Value.ToString();
        string itemType = externalTask.Variables["itemType"].Value.ToString();
        
        _logger.LogInformation("Item type: {itemType}", itemType);

        CompleteResult result = new();
        result.Variables = externalTask.Variables;
        if (itemType == "book")
        {
            BookInfo info = await GetBookDataAsync(isbn);
            string itemId = await _metadataClient.AddBookAsync(info);
            result.Variables[nameof(itemId)] = Variable.String(itemId);
        }
        else if(itemType == "vinyl")
        {

        }
        
        return result;
    }

    private async Task<BookInfo> GetBookDataAsync(string isbn)
    {
        VolumeList books = await _httpClient.GetFromJsonAsync<VolumeList>($"https://www.googleapis.com/books/v1/volumes?q=isbn:{isbn}") 
            ?? throw new Exception("No books found!");
        return books.Items.First().VolumeInfo;
    }

    
}
