# Completion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model** | **str** | ID of the model to use. This should be set to \&quot;suada-v1\&quot; | 
**messages** | [**List[CompletionMessagesInner]**](CompletionMessagesInner.md) | A list of messages comprising the conversation so far. | 
**temperature** | **float** | What sampling temperature to use, between 0 and 2. Higher values like 0.8 will make the output more random, while lower values like 0.2 will make it more focused and deterministic. We generally recommend altering this or top_p but not both. | [optional] 
**top_p** | **float** | An alternative to sampling with temperature, called nucleus sampling, where the model considers the results of the tokens with top_p probability mass. So 0.1 means only the tokens comprising the top 10% probability mass are considered. We generally recommend altering this or temperature but not both. | [optional] 
**frequency_penalty** | **float** | Number between -2.0 and 2.0. Positive values penalize new tokens based on their existing frequency in the text so far, decreasing the model&#39;s likelihood to repeat the same line verbatim. | [optional] 
**presence_penalty** | **float** | Number between -2.0 and 2.0. Positive values penalize new tokens based on whether they appear in the text so far, increasing the model&#39;s likelihood to talk about new topics. | [optional] 
**stop** | **List[str]** | Up to 4 sequences where the API will stop generating further tokens. | [optional] 
**max_tokens** | **float** | The maximum number of tokens that can be generated in the chat completion. The total length of input tokens and generated tokens is limited by the model&#39;s context length. | [optional] 
**n** | **float** | How many chat completion choices to generate for each input message. Note that you will be charged based on the number of generated tokens across all of the choices. Keep n as 1 to minimize costs. | [optional] 
**stream** | **bool** | If set, partial message deltas will be sent, like in ChatGPT. Tokens will be sent as data-only server-sent events as they become available. | [optional] 

## Example

```python
from suada_client.models.completion import Completion

# TODO update the JSON string below
json = "{}"
# create an instance of Completion from a JSON string
completion_instance = Completion.from_json(json)
# print the JSON string representation of the object
print(Completion.to_json())

# convert the object into a dict
completion_dict = completion_instance.to_dict()
# create an instance of Completion from a dict
completion_from_dict = Completion.from_dict(completion_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


