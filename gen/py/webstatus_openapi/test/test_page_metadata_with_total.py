# coding: utf-8

"""
    webstatus.dev API

    A tool to monitor and track the status of all Web Platform features across dimensions that are related to availability and implementation quality across browsers, and adoption by web developers. 

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from webstatus_openapi.models.page_metadata_with_total import PageMetadataWithTotal

class TestPageMetadataWithTotal(unittest.TestCase):
    """PageMetadataWithTotal unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PageMetadataWithTotal:
        """Test PageMetadataWithTotal
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `PageMetadataWithTotal`
        """
        model = PageMetadataWithTotal()
        if include_optional:
            return PageMetadataWithTotal(
                next_page_token = '',
                total = 56
            )
        else:
            return PageMetadataWithTotal(
                total = 56,
        )
        """

    def testPageMetadataWithTotal(self):
        """Test PageMetadataWithTotal"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
