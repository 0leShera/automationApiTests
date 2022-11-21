"""Methods for checking responses"""
from requests import Response
import json


class Cheking():

    """Method for checking status codes"""
    @staticmethod
    def check_status_code(response: Response, status_code):
        assert status_code == response.status_code
        if response.status_code == status_code:
            print(f'Success: Status code = {str(response.status_code)}')
        else:
            print(f'Failed: Status code = {str(response.status_code)}')

    """Method for checking keys from responses"""
    @staticmethod
    def check_json_body(response: Response, expected_value):
        token = json.loads(response.text)
        assert list(token) == expected_value
        print('All keys OK')

    """Method for checking values from responses"""
    @staticmethod
    def check_json_value(response: Response, field_name, expected_value):
        check = response.json()
        check_info = check.get(field_name)
        assert check_info == expected_value
        print(f'Correct response value: {field_name}')

    """Method for checking WORDS values from responses"""
    @staticmethod
    def check_json_word(response: Response, field_name, search_word):
        check = response.json()
        check_info = check.get(field_name)
        if search_word in check_info:
            print(f'Response has search word: {search_word}')
        else:
            print(f'Search word not in answer: {search_word}')
