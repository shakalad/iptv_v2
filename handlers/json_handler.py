import json
import os


class JsonHandler:
    def __init__(self):
        self.__file_path = os.path.join(os.getcwd(), 'json_files/user_data.json')

    def read_file(self):
        with open(self.__file_path, "r") as json_file:
            try:
                data = json.load(json_file)
                return data
            except json.JSONDecodeError:
                return {}

    def get(self, key):
        data = self.read_file()
        return data[key]

    def write_file(self, data):
        with open(self.__file_path, "w") as file:
            json.dump(data, file)

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
