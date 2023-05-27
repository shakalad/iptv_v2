import json
import os


class JsonHandler:
    def __init__(self):
        self.__file_path = os.path.abspath("user_data.json")

    def read_file(self):
        with open(self.__file_path, "r") as json_file:
            try:
                data = json.load(json_file)
                return data
            except json.JSONDecodeError:
                return {}

    def write_file(self, data):
        with open(self.__file_path, "w") as file:
            json.dump(data, file, ident=4)

    def update_data(self, key, value):
        data = self.read_file()
        data[key] = value
        self.write_file(data)

    def delete_data(self, key):
        data = self.read_file()
        if key in data:
            del data[key]
            self.write_file(data)
            return True
        else:
            return False
