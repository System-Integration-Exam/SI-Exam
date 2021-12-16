using Camunda.Worker;

namespace Restock.Services;

[HandlerTopics("fetch-metadata")]
public class CamundaTaskHandler: IExternalTaskHandler
{
    private readonly ILogger<CamundaTaskHandler> _logger;

    public CamundaTaskHandler(ILogger<CamundaTaskHandler> logger)
    {
        _logger = logger;
    }

    public Task<IExecutionResult> HandleAsync(ExternalTask externalTask, CancellationToken cancellationToken)
    {
        _logger.LogInformation(externalTask.Variables["bookISBN"].Value.ToString());
        return Task.FromResult<IExecutionResult>(new CompleteResult());
    }
}
