import json
import os


class JsonHelper:
    def __init__(self, file_name):
        self.base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        self.filename = os.path.join(self.base_dir, "config", f"{file_name}.json")
        self.data = self.load_constants()

    def load_constants(self):
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"Constants file not found: {self.filename}")
            return {}

    def get(self, key):
        return self.data[key]
