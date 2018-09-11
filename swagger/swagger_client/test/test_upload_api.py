# coding: utf-8

"""
    Insights Upload Service

    The Upload Service is designed to ingest payloads from customers and distribute them via a message queue to other Platform services.  # noqa: E501

    OpenAPI spec version: 0.0.1
    Contact: sadams@redhat.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.upload_api import UploadApi  # noqa: E501
from swagger_client.rest import ApiException


class TestUploadApi(unittest.TestCase):
    """UploadApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.upload_api.UploadApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_upload_handler_get(self):
        """Test case for upload_handler_get

        Checks for content-types  # noqa: E501
        """
        pass

    def test_upload_handler_post(self):
        """Test case for upload_handler_post

        Send a file  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
