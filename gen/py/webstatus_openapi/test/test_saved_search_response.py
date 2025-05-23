# coding: utf-8

"""
    webstatus.dev API

    A tool to monitor and track the status of all Web Platform features across dimensions that are related to availability and implementation quality across browsers, and adoption by web developers. 

    The version of the OpenAPI document: 0.1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from webstatus_openapi.models.saved_search_response import SavedSearchResponse

class TestSavedSearchResponse(unittest.TestCase):
    """SavedSearchResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SavedSearchResponse:
        """Test SavedSearchResponse
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SavedSearchResponse`
        """
        model = SavedSearchResponse()
        if include_optional:
            return SavedSearchResponse(
                id = '',
                updated_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                name = '',
                query = '',
                subscription_status = 'none',
                owner_status = 'none'
            )
        else:
            return SavedSearchResponse(
                id = '',
                created_at = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                name = '',
                query = '',
        )
        """

    def testSavedSearchResponse(self):
        """Test SavedSearchResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
