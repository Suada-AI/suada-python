# coding: utf-8

"""
    Suada API

    OpenAPI specification for the Suada API.

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from openapi_client.api.chat_api import ChatApi


class TestChatApi(unittest.TestCase):
    """ChatApi unit test stubs"""

    def setUp(self) -> None:
        self.api = ChatApi()

    def tearDown(self) -> None:
        pass

    def test_chat_completions(self) -> None:
        """Test case for chat_completions

        Create chat completion
        """
        pass


if __name__ == '__main__':
    unittest.main()