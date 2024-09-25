from src.basic_class import APIBasic
import requests
from utils.custom_exception import ConnectionCustomExcept

# import JSON
MAX_PAGE = 5


class HeadHunter(APIBasic):
    """Класс обращения к API HeadHunter."""

    def __init__(self):
        """Иницциализация класса HeadHunter."""
        self.__url = "https://api.hh.ru/vacancies"
        self.__headers = {"User-Agent": "HH-User-agent"}
        self.__params = {"text": "", "page": 0, "per_page": 20}
        self.__vacancies: list[dict] = []

    def __repr__(self):
        return f"{self.__class__.__name__} url:  {self.__url} text:{self.__params['text']}"

    @property
    def url(self):
        return self.__url

    def _connect_api(self, param: str = None):
        """Метод подключение к api hh.ru."""
        res = requests.get(url=self.__url, headers=self.__headers, params=self.__params)
        if res.status_code == 200:
            return res
        else:
            raise ConnectionCustomExcept(f"Сервер ответил ошибкой {res.status_code}")

    def get_vacancies(self, param: str = None):
        """Метод получения вакансий через api hh.ru."""
        if param:
            self.__params["text"] = param
        list_vacancies = []
        for page in range(MAX_PAGE):
            try:
                response_api = self._connect_api()
                vacancies = response_api.json()["items"]
                list_vacancies.extend(vacancies)
                self.__params["page"] = page
            except ConnectionCustomExcept as e:
                print(e)
                return None
        return list_vacancies

    def list_vacancies(self, text=None) -> list[dict]:
        """Метод представления полученых вакансий в виде списка словарей."""
        list_vacancies_filter = []
        vacancies = self.get_vacancies(text)
        for vac in vacancies:
            list_vacancies_filter.append(
                {
                    "name": vac["name"],
                    "salary": vac["salary"],
                    "area": vac["area"],
                    "requirement": vac["snippet"]["requirement"],
                    "alternate_url": vac["alternate_url"],
                }
            )
        return list_vacancies_filter
