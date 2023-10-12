import json

from helpers.api_helper import ApiHelper
from utils.json_helper import JsonHelper
from utils.logger import Logger


class PetServices:
    logger = Logger.log()

    def __init__(self):
        self.req_models = {}
        self.__api_helper = ApiHelper()
        self.__config_helper = JsonHelper("config")
        self.__api_helper.set_base_url(self.__config_helper.get("apiUrl"))

    def pet_upload_image(self, pet_id, additional_metadata, file_name):
        self.__api_helper.set_endpoint(f"/pet/{pet_id}/uploadImage")
        self.__api_helper.add_request_body({'additionalMetadata': additional_metadata})
        self.__api_helper.add_request_files(file_name)
        response = self.__api_helper.send_request("post_with_file")
        return response

    def add_new_pet(self, req_body):
        self.__api_helper.add_content_type("json")
        self.__api_helper.set_endpoint("/pet")
        self.__api_helper.add_request_body(req_body)
        response = self.__api_helper.send_request("post_with_raw")
        return response

    def update_pet(self, req_body):
        self.__api_helper.add_content_type("json")
        self.__api_helper.set_endpoint("/pet")
        self.__api_helper.add_request_body(req_body)
        response = self.__api_helper.send_request("put_with_raw")
        return response

    def find_pet_by_status(self, status):
        self.__api_helper.set_endpoint(f"/pet/findByStatus?status={status}")
        response = self.__api_helper.send_request("get")
        return response

    def get_pet_by_id(self, pet_id):
        self.__api_helper.set_endpoint(f"/pet/{pet_id}")
        response = self.__api_helper.send_request("get")
        return response

    def update_pet_with_form_data(self, pet_id, form_data):
        self.__api_helper.add_content_type("form")
        self.__api_helper.set_endpoint(f"/pet/{pet_id}")
        self.__api_helper.add_header('Accept-Encoding', 'gzip, deflate, br')
        self.__api_helper.add_header('Accept', '*/*')
        self.__api_helper.add_request_body(form_data)
        response = self.__api_helper.send_request("post_with_form")
        return response

    def delete_pet(self, pet_id):
        self.__api_helper.set_endpoint(f"/pet/{pet_id}")
        response = self.__api_helper.send_request("delete")
        return response

    def get_req_models(self):
        self.req_models = {
            "addNewPet": {
                "id": 0,
                "category": {
                    "id": 0,
                    "name": "string"
                },
                "name": "doggie",
                "photoUrls": [
                    "string"
                ],
                "tags": [
                    {
                        "id": 0,
                        "name": "string"
                    }
                ],
                "status": "available"
            },
            "updatePet": {
                "id": 0,
                "category": {
                    "id": 0,
                    "name": "string"
                },
                "name": "doggie",
                "photoUrls": [
                    "string"
                ],
                "tags": [
                    {
                        "id": 0,
                        "name": "string"
                    }
                ],
                "status": "available"
            },
            "updatePetWithFormData": {
                "name": "Animal",
                "status": "available;pending;sold"
            }
        }
        return self.req_models
