import json
import os


class JsonEditor:
    def __init__(self):
        self.directory = 'saved_data'
        self.file_path = os.path.join(self.directory, 'vacancies.json')
        self.create_directory()

    def create_directory(self):
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)

    def add_vacancy(self, vacancy_data):
        with open(self.file_path, mode='w', encoding='utf-8') as file:
            json_file = json.dumps(vacancy_data, indent=4, ensure_ascii=False)
            file.write(json_file)

    def clear_file(self):
        with open(self.file_path, 'w', encoding='utf-8') as file:
            file.write("")
