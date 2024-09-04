# suada_client.ChatApi

All URIs are relative to *https://api.suada.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**chat_completions**](ChatApi.md#chat_completions) | **POST** /v1/chat/completions | Create chat completion


# **chat_completions**
> CompletionResult chat_completions(completion)

Create chat completion

### Example

* Bearer (JWT) Authentication (BearerAuth):

```python
import suada_client
from suada_client.models.completion import Completion
from suada_client.models.completion_result import CompletionResult
from suada_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.suada.ai
# See configuration.py for a list of all supported configuration parameters.
configuration = suada_client.Configuration(
    host = "https://api.suada.ai"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): BearerAuth
configuration = suada_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with suada_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = suada_client.ChatApi(api_client)
    completion = suada_client.Completion() # Completion | 

    try:
        # Create chat completion
        api_response = api_instance.chat_completions(completion)
        print("The response of ChatApi->chat_completions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ChatApi->chat_completions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **completion** | [**Completion**](Completion.md)|  | 

### Return type

[**CompletionResult**](CompletionResult.md)

### Authorization

[BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful completion |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

