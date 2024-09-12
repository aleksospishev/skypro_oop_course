from src.basic_class import API
import requests


class HeadHunter(API):
    "Класс обращения к API HeadHunter."

    def __init__(self):
        "Иницциализация класса HeadHunter"
        self.__url = 'https://api.hh.ru/vacancies'
        self.__headers = {"User-Agent": "HH-User-Agent"}
        self.__params = {"text": "", "page": 0, "per_page": 100}
        self.__vacancies: list[dict] = []

    @property
    def __str__(cls):
        return f"{cls.name}: {self.__url},{self.__params['text']}"

