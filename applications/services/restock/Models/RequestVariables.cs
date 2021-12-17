using Camunda.Worker;

namespace Restock.Models;

public class RequestVariables
{
    public RequestVariables(string itemType, string requestText, long existingItemCount, long storeId, string itemId)
    {
        ItemType = Variable.String(itemType);
        RequestText = Variable.String(requestText);
        ExistingItemCount = Variable.Long(existingItemCount);
        StoreId = Variable.Long(storeId);
        ItemId = Variable.String(itemId);
    }

    public Variable ItemType { get; }
    public Variable RequestText { get; }
    public Variable ExistingItemCount { get; }
    public Variable StoreId { get; }
    public Variable ItemId { get; set; }

}