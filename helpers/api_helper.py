import mimetypes

import requests
import time
import os
import json
from utils.logger import Logger


class ApiHelper:
    logger = Logger.log()

    def __init__(self):
        self.__request = requests.Session()
        self.__headers = {}
        self.__response = None
        self.__response_body = None
        self.__response_time = None
        self.__baseUrl = None
        self.__url = None
        self.__req_body = None
        self.__files = None
        self.__request_type = None

    def set_base_url(self, base_url):
        self.__baseUrl = base_url

    def set_endpoint(self, endpoint):
        self.__url = f"{self.__baseUrl}{endpoint}"

    def add_content_type(self, content_type):
        content_types = {
            'json': 'application/json',
            'html': 'text/html',
            'xml': 'application/xml',
            'plain': 'text/plain',
            'form': 'application/x-www-form-urlencoded',
            'multipart': 'multipart/form-data'
        }
        self.__headers['Content-Type'] = content_types[content_type]

    def add_authorization(self, token):
        self.__headers['Authorization'] = token

    def add_header(self, key, value):
        self.__headers[key] = value

    def add_request_body(self, body):
        self.__req_body = body

    def add_request_files(self, file_name):
        if file_name:
            base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
            file_path = os.path.join(base_dir, "config", "test_data", file_name)

            mime_type, _ = mimetypes.guess_type(file_path)
            if mime_type is None:
                mime_type = 'application/octet-stream'
            self.__files = {'file': (os.path.basename(file_path), open(file_path, 'rb'), mime_type)}
        else:
            self.__files = file_name
        return self.__files

    def send_request(self, request_type):
        self.__request_type = request_type
        start_time = time.time()

        if request_type == 'get':
            self.__response = self.__request.get(self.__url, headers=self.__headers)
        elif request_type == 'post_with_raw':
            self.__response = self.__request.post(self.__url, headers=self.__headers, data=json.dumps(self.__req_body))
        elif request_type == 'post_with_form':
            self.__response = self.__request.post(self.__url, headers=self.__headers, data=self.__req_body)
        elif request_type == 'post_with_file':
            self.__response = self.__request.post(self.__url, headers=self.__headers, data=self.__req_body,
                                                  files=self.__files)
        elif request_type == 'put_with_form':
            self.__response = self.__request.put(self.__url, headers=self.__headers, data=self.__req_body)
        elif request_type == 'put_with_raw':
            self.__response = self.__request.put(self.__url, headers=self.__headers, data=json.dumps(self.__req_body))
        elif request_type == 'put_with_file':
            self.__response = self.__request.put(self.__url, headers=self.__headers, data=self.__req_body,
                                                 files=self.__files)
        elif request_type == 'delete':
            self.__response = self.__request.delete(self.__url, headers=self.__headers)
        elif request_type == 'patch':
            self.__response = self.__request.patch(self.__url, headers=self.__headers, data=self.__req_body)

        self.__response_time = (time.time() - start_time) * 1000  # ms
        try:
            response_json = self.__response.json()
            if isinstance(response_json, list):
                self.__response_body = response_json
            else:
                self.__response_body = response_json if response_json else None
        except ValueError as e:
            self.__response_body = self.__response.text
            print(f"JSON error: {e}")

        self.log_request_response_info()
        return {
            'data': self.__response_body,
            'response': self.__response,
            'status': self.__response.status_code,
            'time': self.__response_time
        }

    def log_request_response_info(self):
        self.logger.info(
            f"\n\n*********** REQUEST ***********\n"
            f"Request Type: {self.__request_type}\n"
            f"Request Headers: {self.__headers}\n"
            f"Request URL: {self.__url}\n"
            f"Request Body: {json.dumps(self.__req_body, indent=2)}\n"
            f"*********** RESPONSE ***********\n"
            f"Response Time: {self.__response_time} ms\n"
            f"Response Status: {self.__response.status_code}\n"
            f"Response Body: {json.dumps(self.__response_body, indent=2)}\n"
            f"*********** REQUEST-RESPONSE END ***********\n"
        )
