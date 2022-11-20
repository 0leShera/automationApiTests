from utils.api import Google_maps_api
from utils.cheking import Cheking
from requests import Response
import json

"""Create, update and delete new location"""


class Test_create_place():

    def test_create_new_place(self):

        print('\nMethod POST')
        result_post: Response = Google_maps_api.create_new_place()
        check_post = result_post.json()
        place_id = check_post.get('place_id')
        Cheking.check_status_code(result_post, 200)
        Cheking.check_json_body(result_post, ['status', 'place_id', 'scope', 'reference', 'id'])
        # token = json.loads(result_post.text)    # Get keys from JSON response
        # print(list(token))

        print('\nMethod GET for POST')
        result_get: Response = Google_maps_api.get_new_place(place_id)
        Cheking.check_status_code(result_get, 200)
        Cheking.check_json_body(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])

        print('\nMethod PUT')
        result_put: Response = Google_maps_api.put_new_place(place_id)
        Cheking.check_status_code(result_put, 200)
        Cheking.check_json_body(result_put, ['msg'])

        print('\nMethod GET for PUT')
        result_get: Response = Google_maps_api.get_new_place(place_id)
        Cheking.check_status_code(result_get, 200)
        Cheking.check_json_body(result_get, ['location', 'accuracy', 'name', 'phone_number', 'address', 'types', 'website', 'language'])

        print('\nMethod DELETE')
        result_delete: Response = Google_maps_api.delete_new_place(place_id)
        Cheking.check_status_code(result_delete, 200)
        Cheking.check_json_body(result_delete, ['status'])

        print('\nMethod GET for DELETE')
        result_get: Response = Google_maps_api.get_new_place(place_id)
        Cheking.check_status_code(result_get, 404)
        Cheking.check_json_body(result_get, ['msg'])

        print()
        print('*' * 20 + 'Test create, update and delete new location ended.' + '*' * 20)
