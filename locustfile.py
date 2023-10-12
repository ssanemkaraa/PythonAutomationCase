import json
from locust import HttpUser, task

class PetServicesUser(HttpUser):

    @task
    def pet_upload_image(self):
        pet_id = 2
        additional_metadata = {"key": "value"}
        file_name = "test_image.jpg"
        with open(file_name, "rb") as f:
            response = self.client.post(f"/pet/{pet_id}/uploadImage", data={"additionalMetadata": json.dumps(additional_metadata)}, files={"file": f})

    @task
    def add_new_pet(self):
        req_body = json.dumps(self.user.req_models["addNewPet"])
        response = self.client.post("/pet", headers={"Content-Type": "application/json"}, data=req_body)

    @task
    def update_pet(self):
        req_body = json.dumps(self.user.req_models["updatePet"])
        response = self.client.put("/pet", headers={"Content-Type": "application/json"}, data=req_body)

    @task
    def find_pet_by_status(self):
        status = "available"
        response = self.client.get(f"/pet/findByStatus?status={status}")

    @task
    def get_pet_by_id(self):
        pet_id = 2
        response = self.client.get(f"/pet/{pet_id}")

    @task
    def update_pet_with_form_data(self):
        pet_id = 2
        form_data = {"name": "Animal", "status": "available"}
        response = self.client.post(f"/pet/{pet_id}", data=form_data)

    @task
    def delete_pet(self):
        pet_id = 2
        response = self.client.delete(f"/pet/{pet_id}")
