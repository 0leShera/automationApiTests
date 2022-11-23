import allure
from utils.api import Google_maps_api
from utils.cheking import Cheking
from requests import Response
# import json

"""Create, update and delete new location"""


@allure.epic('Test CRUD for location.')
class Test_create_place():

    @allure.description('Test case crate read update delete for location.')
    def test_create_new_place(self):

        print('\nMethod POST')
        result_post: Response = Google_maps_api.create_new_place()
        check_post = result_post.json()
        place_id = check_post.get('place_id')
        Cheking.check_status_code(result_post, 200)
        Cheking.check_json_body(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])
        # token = json.loads(result_post.text)    # Get keys from JSON response
        # print(list(token))
        Cheking.check_json_value(result_post, 'status', expected_value='OK')

        print('\nMethod GET for POST')
        result_get: Response = Google_maps_api.get_new_place(place_id)
        Cheking.check_status_code(result_get, 200)
        Cheking.check_json_body(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types',
                                             'website', 'language'])
        Cheking.check_json_value(result_get, 'address', expected_value='29, side layout, cohen 09')

        print('\nMethod PUT')
        result_put: Response = Google_maps_api.put_new_place(place_id)
        Cheking.check_status_code(result_put, 200)
        Cheking.check_json_body(result_put, ['msg'])
        Cheking.check_json_value(result_put, 'msg', expected_value='Address successfully updated')

        print('\nMethod GET for PUT')
        result_get: Response = Google_maps_api.get_new_place(place_id)
        Cheking.check_status_code(result_get, 200)
        Cheking.check_json_body(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types',
                                             'website', 'language'])
        Cheking.check_json_value(result_get, 'address', expected_value='100 Lenina str, RU, Msk')

        print('\nMethod DELETE')
        result_delete: Response = Google_maps_api.delete_new_place(place_id)
        Cheking.check_status_code(result_delete, 200)
        Cheking.check_json_body(result_delete, ['status'])
        Cheking.check_json_value(result_delete, 'status', expected_value='OK')

        print('\nMethod GET for DELETE')
        result_get: Response = Google_maps_api.get_new_place(place_id)
        Cheking.check_status_code(result_get, 404)
        Cheking.check_json_body(result_get, ['msg'])
        Cheking.check_json_value(result_get, 'msg', expected_value='Get operation failed, looks like place_id  '
                                                                   'doesn\'t exists')
        # Cheking.check_json_word(result_get, 'msg', search_word='failed')

        print()
        print('*' * 20 + 'Test create, update and delete new location ended.' + '*' * 20)
