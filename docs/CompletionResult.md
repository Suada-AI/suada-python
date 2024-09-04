# CompletionResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**object** | **str** |  | [optional] 
**created** | **float** |  | [optional] 
**model** | **str** |  | [optional] 
**system_fingerprint** | **str** |  | [optional] 
**choices** | [**List[CompletionResultChoicesInner]**](CompletionResultChoicesInner.md) |  | [optional] 
**usage** | [**CompletionResultUsage**](CompletionResultUsage.md) |  | [optional] 

## Example

```python
from suada_client.models.completion_result import CompletionResult

# TODO update the JSON string below
json = "{}"
# create an instance of CompletionResult from a JSON string
completion_result_instance = CompletionResult.from_json(json)
# print the JSON string representation of the object
print(CompletionResult.to_json())

# convert the object into a dict
completion_result_dict = completion_result_instance.to_dict()
# create an instance of CompletionResult from a dict
completion_result_from_dict = CompletionResult.from_dict(completion_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


