# CompletionResultChoicesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**index** | **float** |  | [optional] 
**message** | [**CompletionResultChoicesInnerMessage**](CompletionResultChoicesInnerMessage.md) |  | [optional] 
**logprobs** | **object** |  | [optional] 
**finish_reason** | **str** |  | [optional] 

## Example

```python
from suada_client.models.completion_result_choices_inner import CompletionResultChoicesInner

# TODO update the JSON string below
json = "{}"
# create an instance of CompletionResultChoicesInner from a JSON string
completion_result_choices_inner_instance = CompletionResultChoicesInner.from_json(json)
# print the JSON string representation of the object
print(CompletionResultChoicesInner.to_json())

# convert the object into a dict
completion_result_choices_inner_dict = completion_result_choices_inner_instance.to_dict()
# create an instance of CompletionResultChoicesInner from a dict
completion_result_choices_inner_from_dict = CompletionResultChoicesInner.from_dict(completion_result_choices_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


