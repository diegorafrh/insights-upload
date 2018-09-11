# swagger_client.VersionApi

All URIs are relative to *http://localhost:8888*

Method | HTTP request | Description
------------- | ------------- | -------------
[**version_handler_get**](VersionApi.md#version_handler_get) | **GET** /api/v1/version | Get the application version


# **version_handler_get**
> version_handler_get()

Get the application version

Return the current application version

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.VersionApi()

try:
    # Get the application version
    api_instance.version_handler_get()
except ApiException as e:
    print("Exception when calling VersionApi->version_handler_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

