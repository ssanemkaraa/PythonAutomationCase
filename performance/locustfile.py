import json
import os

from locust import HttpUser, task

from services.pet_services import PetServices


class PetServicesUser(HttpUser):
    pet_services = PetServices()
    req_models = pet_services.get_req_models()
    pet_id = 2
    @task
    def pet_upload_image(self):
        additional_metadata = {"key": "value"}
        file_name = os.path.join('../config', 'test_data', '38KB.jpg')

        with open(file_name, "rb") as f:
            self.client.post(f"/pet/{self.pet_id}/uploadImage",
                                        data={"additionalMetadata": json.dumps(additional_metadata)}, files={"file": f})

    @task
    def add_new_pet(self):
        req_body = json.dumps(self.req_models["addNewPet"])
        self.client.post("/pet", headers={"Content-Type": "application/json"}, data=req_body)

    @task
    def update_pet(self):
        req_body = json.dumps(self.req_models["updatePet"])
        self.client.put("/pet", headers={"Content-Type": "application/json"}, data=req_body)

    @task
    def find_pet_by_status(self):
        status = "available"
        self.client.get(f"/pet/findByStatus?status={status}")

    @task
    def get_pet_by_id(self):
        self.client.get(f"/pet/{self.pet_id}")

    @task
    def update_pet_with_form_data(self):
        form_data = {"name": "Animal", "status": "available"}
        self.client.post(f"/pet/{self.pet_id}", data=form_data)
