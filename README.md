# suada-client
OpenAPI specification for the Suada API.

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.0
- Package version: 1.0.0
- Generator version: 7.8.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 3.7+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import suada_client
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import suada_client
```

### Tests

Execute `pytest` to run the tests.

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python

import suada_client
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
        api_response = api_instance.generate(completion)
        print("The response of ChatApi->generate:\n")
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling ChatApi->generate: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://api.suada.ai*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ChatApi* | [**generate**](docs/ChatApi.md#generate) | **POST** /v1/chat/completions | Create chat completion


## Documentation For Models

 - [Completion](docs/Completion.md)
 - [CompletionMessagesInner](docs/CompletionMessagesInner.md)
 - [CompletionResult](docs/CompletionResult.md)
 - [CompletionResultChoicesInner](docs/CompletionResultChoicesInner.md)
 - [CompletionResultChoicesInnerMessage](docs/CompletionResultChoicesInnerMessage.md)
 - [CompletionResultUsage](docs/CompletionResultUsage.md)


<a id="documentation-for-authorization"></a>
## Documentation For Authorization


Authentication schemes defined for the API:
<a id="BearerAuth"></a>
### BearerAuth

- **Type**: Bearer authentication (JWT)


## Author




