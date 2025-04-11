from src.basic_class import FileManager
from src.vacancies import Vacancy
import json
import os


class JsonFileManager(FileManager):
    def __init__(self, path):
        self.__path = os.path.abspath(path)

    def write_data(self, vacancies):
        with open(self.__path, "w", encoding="utf-8") as f:
            json.dump(vacancies, f, ensure_ascii=False, indent=4)

    def load_data(self):
        with open(self.__path, "r", encoding="utf-8") as f:
            data = json.load(f)
        vacancy_list = []
        for vac in data:
            vacancy_list.append(Vacancy(**vac))
        return vacancy_list

    def delete_data(self):
        open(self.__path, "w").close()
