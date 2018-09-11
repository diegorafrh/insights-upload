# swagger_client.StatusApi

All URIs are relative to *http://localhost:8888*

Method | HTTP request | Description
------------- | ------------- | -------------
[**status_handler_get**](StatusApi.md#status_handler_get) | **GET** /api/v1/status | Check if the application is online


# **status_handler_get**
> status_handler_get()

Check if the application is online

Return a json that shows which system/api is running (or not)

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StatusApi()

try:
    # Check if the application is online
    api_instance.status_handler_get()
except ApiException as e:
    print("Exception when calling StatusApi->status_handler_get: %s\n" % e)
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

