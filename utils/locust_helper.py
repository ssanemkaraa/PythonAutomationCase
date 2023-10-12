from locust import HttpUser, task, between


class SearchUser(HttpUser):
    wait_time = between(1, 2)

    @task
    def search_product(self):
        response = self.client.get("/arama?q=laptop")
        if response.status_code == 200:
            self.environment.runner.environment.events.request_success.fire(
                request_type="GET",
                name="search_product",
                response_time=response.elapsed.total_seconds() * 1000,
                response_length=len(response.content),
            )
        else:
            self.environment.runner.environment.events.request_failure.fire(
                request_type="GET",
                name="search_product",
                response_time=response.elapsed.total_seconds() * 1000,
                exception="Failed to search product",
            )
