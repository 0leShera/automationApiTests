from utils.http_methods import Http_methods

"""Methods for testing Google Maps api"""

base_url = 'https://rahulshettyacademy.com'  # base url for all requests
key = '?key=qaclick123'  # param for all requests


class Google_maps_api():

    """Method for create new place (post)"""
    @staticmethod
    def create_new_place():
        json_for_crate_new_place = {
            "location": {
                "lat": -38.383494,
                "lng": 33.427362
            },
            "accuracy": 50,
            "name": "Frontline house",
            "phone_number": "(+91) 983 893 3937",
            "address": "29, side layout, cohen 09",
            "types": [
                "shoe park",
                "shop"
            ],
            "website": "http://google.com",
            "language": "French-IN"
        }

        post_resource = '/maps/api/place/add/json'    # Resource for method post
        post_url = base_url + post_resource + key
        print(post_url)
        result_post = Http_methods.post(post_url, json_for_crate_new_place)
        print(result_post.text)
        return result_post

    """Method for check new place (get)"""
    @staticmethod
    def get_new_place(place_id):

        get_resource = '/maps/api/place/get/json'    # Resource for method get
        get_url = base_url + get_resource + key + '&place_id=' + place_id
        print(get_url)
        result_get = Http_methods.get(get_url)
        print(result_get.text)
        return result_get

    """Method for update new place (put)"""
    @staticmethod
    def put_new_place(place_id):
        json_for_update_new_place = {
            "place_id": place_id,
            "address": "100 Lenina str, RU, Msk",
            "key": "qaclick123"
        }
        put_resource = '/maps/api/place/update/json'    # Resource for method put
        put_url = base_url + put_resource + key
        print(put_url)
        result_put = Http_methods.put(put_url, json_for_update_new_place)
        print(result_put.text)
        return result_put

    """Method for delete new place (delete)"""
    @staticmethod
    def delete_new_place(place_id):
        json_for_delete_new_place = {
            "place_id": place_id
        }
        delete_resource = '/maps/api/place/delete/json'    # Resource for method delete
        delete_url = base_url + delete_resource + key
        print(delete_url)
        result_delete = Http_methods.put(delete_url, json_for_delete_new_place)
        print(result_delete.text)
        return result_delete
