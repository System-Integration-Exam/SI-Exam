using System.Net;

namespace Restock.Services;

public class CamundaDeploymentService
{
    private readonly ILogger<CamundaDeploymentService> _logger;
    private readonly IHttpClientFactory _clientFactory;
    private const string CamundaDeploymentSource = "Restock Service";

    public CamundaDeploymentService(ILogger<CamundaDeploymentService> logger, IHttpClientFactory clientFactory)
    {
        _logger = logger;
        _clientFactory = clientFactory;
    }

    public async Task RemoveDefaultDeployments()
    {
        HttpClient client = _clientFactory.CreateClient("camundaClient");
        IEnumerable<CamundaDeployment> deployments = await client.GetFromJsonAsync<IEnumerable<CamundaDeployment>>("deployment")
            ?? Enumerable.Empty<CamundaDeployment>();

        foreach (CamundaDeployment deployment in deployments)
        {
            if(deployment.Source != CamundaDeploymentSource)
                await client.DeleteAsync($"deployment/{deployment.Id}?cascade=true");
        }

    }
    public async Task DeployRestockModelAsync()
    {
        MultipartFormDataContent content = await GetMultipartFormDataContentAsync();

        HttpClient client = _clientFactory.CreateClient("camundaClient");
        HttpResponseMessage response = await client.PostAsync("deployment/create", content);

        if (response.IsSuccessStatusCode)
            _logger.LogInformation("Succesfully deployed files to camunda.");
        else
        {
            _logger.LogError("Something went wrong under deployment to camunda. Server responded with: {statusCode} {statusName} {reason}", (int)response.StatusCode, response.StatusCode, response.ReasonPhrase);
            _logger.LogError(response.RequestMessage?.ToString());
        }
    }

    private async Task<MultipartFormDataContent> GetMultipartFormDataContentAsync()
    {
        MultipartFormDataContent content = new();
        content.Add(await StringToContentAsync("restock_deployment"), "deployment-name");
        content.Add(await StringToContentAsync("true"), "deploy-changed-only");
        content.Add(await StringToContentAsync(CamundaDeploymentSource), "deployment-source");

        foreach (string fileName in new[] { "restock_model.bpmn", "restock_rules.dmn", "bookContract_form.form", "vinylContract_form.form", "buyItem_form.form" })
            content.Add(await GetCamundaFileAsContentAsync(fileName), fileName, fileName);
        
        return content;
    }

    private async Task<StreamContent> StringToContentAsync(string value)
    {
        MemoryStream stream = new();
        StreamWriter writer = new(stream);

        await writer.WriteAsync(value);
        await writer.FlushAsync();
        stream.Position = 0;

        return new StreamContent(stream);
    }

    private async Task<StreamContent> GetCamundaFileAsContentAsync(string fileName)
    {
        HttpClient client = _clientFactory.CreateClient();

        string fileContent = await client.GetStringAsync("https://raw.githubusercontent.com/System-Integration-Exam/SI-Exam/main/applications/bpmn/" + fileName);
        return await StringToContentAsync(fileContent);
    }

    private class CamundaDeployment
    {
        public string Id { get; set; }
        public string Name { get; set; }
        public string Source { get; set; }
    }
}
