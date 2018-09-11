# swagger_client.BaseApi

All URIs are relative to *http://localhost:8888*

Method | HTTP request | Description
------------- | ------------- | -------------
[**root_handler_get**](BaseApi.md#root_handler_get) | **GET** / | Checks if the application is running


# **root_handler_get**
> root_handler_get()

Checks if the application is running

Return a simple string 'boop' to verify if the application is running

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BaseApi()

try:
    # Checks if the application is running
    api_instance.root_handler_get()
except ApiException as e:
    print("Exception when calling BaseApi->root_handler_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

