# swagger_client.UploadApi

All URIs are relative to *http://localhost:8888*

Method | HTTP request | Description
------------- | ------------- | -------------
[**upload_handler_get**](UploadApi.md#upload_handler_get) | **GET** /api/v1/upload | Checks for content-types
[**upload_handler_post**](UploadApi.md#upload_handler_post) | **POST** /api/v1/upload | Send a file


# **upload_handler_get**
> upload_handler_get()

Checks for content-types

Return which content types are available

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UploadApi()

try:
    # Checks for content-types
    api_instance.upload_handler_get()
except ApiException as e:
    print("Exception when calling UploadApi->upload_handler_get: %s\n" % e)
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

# **upload_handler_post**
> upload_handler_post(upload)

Send a file

Send on file to be analyzed just like insights-client would do

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UploadApi()
upload = '/path/to/file.txt' # file | Select the tar.gz file to upload. You may find a file example at PROJECT_PATH/swagger/payload.tar.gz

try:
    # Send a file
    api_instance.upload_handler_post(upload)
except ApiException as e:
    print("Exception when calling UploadApi->upload_handler_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **upload** | **file**| Select the tar.gz file to upload. You may find a file example at PROJECT_PATH/swagger/payload.tar.gz | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

