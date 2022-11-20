"""Methods for checking responses"""
from requests import Response
import json


class Cheking():

    """Method for checking status codes"""
    @staticmethod
    def check_status_code(response: Response, status_code):
        assert status_code == response.status_code
        if response.status_code == status_code:
            print('Success: Status code = ' + str(response.status_code))
        else:
            print('Failed: Status code = ' + str(response.status_code))

    """Method for checking keys from responses"""
    @staticmethod
    def check_json_body(response: Response, expected_value):
        token = json.loads(response.text)
        assert list(token) == expected_value
        print('All keys OK')
