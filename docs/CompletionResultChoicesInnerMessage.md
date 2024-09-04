# CompletionResultChoicesInnerMessage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** |  | [optional] 
**content** | **str** |  | [optional] 

## Example

```python
from suada_client.models.completion_result_choices_inner_message import CompletionResultChoicesInnerMessage

# TODO update the JSON string below
json = "{}"
# create an instance of CompletionResultChoicesInnerMessage from a JSON string
completion_result_choices_inner_message_instance = CompletionResultChoicesInnerMessage.from_json(json)
# print the JSON string representation of the object
print(CompletionResultChoicesInnerMessage.to_json())

# convert the object into a dict
completion_result_choices_inner_message_dict = completion_result_choices_inner_message_instance.to_dict()
# create an instance of CompletionResultChoicesInnerMessage from a dict
completion_result_choices_inner_message_from_dict = CompletionResultChoicesInnerMessage.from_dict(completion_result_choices_inner_message_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


