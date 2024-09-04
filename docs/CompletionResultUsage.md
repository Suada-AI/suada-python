# CompletionResultUsage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prompt_tokens** | **float** |  | [optional] 
**completion_tokens** | **float** |  | [optional] 
**total_tokens** | **float** |  | [optional] 

## Example

```python
from suada_client.models.completion_result_usage import CompletionResultUsage

# TODO update the JSON string below
json = "{}"
# create an instance of CompletionResultUsage from a JSON string
completion_result_usage_instance = CompletionResultUsage.from_json(json)
# print the JSON string representation of the object
print(CompletionResultUsage.to_json())

# convert the object into a dict
completion_result_usage_dict = completion_result_usage_instance.to_dict()
# create an instance of CompletionResultUsage from a dict
completion_result_usage_from_dict = CompletionResultUsage.from_dict(completion_result_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


