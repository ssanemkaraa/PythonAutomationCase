import requests
from services.pet_services import PetServices


class TestApiPet:
    pet_services = PetServices()
    pet_id = "2"

    # ===================== upload image =====================
    def test_pet_upload_image_png_happy_path(self):
        response = self.pet_services.pet_upload_image(self.pet_id, "test", "4MB.png")
        assert response['response'].status_code == 200
        assert response['data']['code'] == 200
        assert response['data']['type'] == "unknown"
        assert "File uploaded to" in response['data']['message']

    def test_pet_upload_image_jpg_happy_path(self):
        response = self.pet_services.pet_upload_image(self.pet_id, "test", "4MB.jpg")
        assert response['response'].status_code == 200
        assert response['data']['code'] == 200
        assert response['data']['type'] == "unknown"
        assert "File uploaded to" in response['data']['message']

    def test_pet_upload_image_mp4_happy_path(self):
        response = self.pet_services.pet_upload_image(self.pet_id, "test", "2MB.mp4")
        assert response['response'].status_code == 200
        assert response['data']['code'] == 200
        assert response['data']['type'] == "unknown"
        assert "File uploaded to" in response['data']['message']

    def test_pet_upload_image_empty_file_negative(self):
        response = self.pet_services.pet_upload_image(self.pet_id, "tst", "")
        assert response['response'].status_code == 415

    # ===================== add new pet =====================
    def test_add_new_pet_random_id_happy_path(self):
        req_body = self.pet_services.get_req_models().get("addNewPet")
        response = self.pet_services.add_new_pet(req_body)
        assert response['response'].status_code == 200
        assert response['data']['id'] is not None
        assert response['data']['category'] == req_body['category']
        assert response['data']['category'] == req_body['category']
        assert response['data']['tags'] == req_body['tags']
        assert response['data']['photoUrls'] == req_body['photoUrls']
        assert response['data']['status'] == req_body['status']

    def test_add_new_pet_specified_id_happy_path(self):
        req_body = self.pet_services.get_req_models().get("addNewPet")
        req_body['id'] = 135434354
        response = self.pet_services.add_new_pet(req_body)
        assert response['response'].status_code == 200
        assert response['data']['id'] == req_body['id']
        assert response['data']['category'] == req_body['category']
        assert response['data']['category'] == req_body['category']
        assert response['data']['tags'] == req_body['tags']
        assert response['data']['photoUrls'] == req_body['photoUrls']
        assert response['data']['status'] == req_body['status']

    # ===================== update pet =====================
    def test_update_pet_specified_id_happy_path(self):
        req_body = self.pet_services.get_req_models().get("updatePet")
        req_body['id'] = 135434354
        response = self.pet_services.update_pet(req_body)
        data = response['data']
        assert response['response'].status_code == 200
        assert data['id'] == req_body['id']
        assert data['category'] == req_body['category']
        assert data['category'] == req_body['category']
        assert data['tags'] == req_body['tags']
        assert data['photoUrls'] == req_body['photoUrls']
        assert data['status'] == req_body['status']

    # ===================== find pet by status =====================
    def test_find_pet_by_status_happy_path(self):
        response_avaliable = self.pet_services.find_pet_by_status("avaliable")
        assert response_avaliable['response'].status_code == 200

        response_pending = self.pet_services.find_pet_by_status("pending")
        assert response_pending['response'].status_code == 200

        response_sold = self.pet_services.find_pet_by_status("sold")
        assert response_sold['response'].status_code == 200

    # ===================== get pet by id =====================
    def test_get_pet_by_id_happy_path(self):
        response = self.pet_services.get_pet_by_id(self.pet_id)
        assert response['response'].status_code == 200

    # ===================== update with form =====================
    def test_update_with_form_happy_path(self):
        form_data = self.pet_services.get_req_models().get("updatePetWithFormData")
        response = self.pet_services.update_pet_with_form_data(self.pet_id, form_data)
        assert response['response'].status_code == 200

    # ===================== delete pet =====================
    def test_delete_pet_happy_path(self):
        response = self.pet_services.delete_pet(self.pet_id)
        assert response['response'].status_code == 200