# CompletionMessagesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**role** | **str** | The role of the message&#39;s author. | [optional] 
**content** | **str** | The contents of the message. | [optional] 
**name** | **str** | An optional name for the participant. Provides the model information to differentiate between participants of the same role. | [optional] 

## Example

```python
from suada_client.models.completion_messages_inner import CompletionMessagesInner

# TODO update the JSON string below
json = "{}"
# create an instance of CompletionMessagesInner from a JSON string
completion_messages_inner_instance = CompletionMessagesInner.from_json(json)
# print the JSON string representation of the object
print(CompletionMessagesInner.to_json())

# convert the object into a dict
completion_messages_inner_dict = completion_messages_inner_instance.to_dict()
# create an instance of CompletionMessagesInner from a dict
completion_messages_inner_from_dict = CompletionMessagesInner.from_dict(completion_messages_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


