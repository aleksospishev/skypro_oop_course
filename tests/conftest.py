from src.vacancies import Vacancy
import pytest


@pytest.fixture
def vacancy_test():
    vacs = [
        {
            "name": "Strong Junior Backend разработчик",
            "salary": {"from": 250000, "to": 500000},
            "area": {
                "name": "Алматы",
            },
            "requirement": "Опыт работы с Django/DRF. - Опыт работы с Redis, Docker, и похожие технологии. ",
            "alternate_url": "url2",
        },
        {
            "name": "Backend-разработчик",
            "salary": None,
            "area": {"name": "Астана"},
            "requirement": "...Java и python от 3 лет. Глубокие знания и опыт работы. ",
            "alternate_url": "url2",
        },
    ]
    return vacs


@pytest.fixture
def vacancy_test_list():
    vacanciies = [
        Vacancy("Backend-разработчик", {"name": "Астана"}, "url2", "python от 3 лет. знания и опыт работы. "),
        Vacancy(
            "Junior",
            {"name": "Москва"},
            "url3",
            "python. Глубокие знания и опыт работы.",
            {"from": 30000, "to": 50000},
        ),
        Vacancy("Senior", {"name": "Баку"}, "url4", "Python от 2 лет", {"from": 70000, "to": 100000}),
    ]
    return vacanciies


@pytest.fixture
def data_file_manager():
    vac = [
        {
            "name": "Strong Junior Backend разработчик",
            "salary": {"from": 250000, "to": 500000, "currency": "KZT"},
            "area": {"id": "160", "name": "Алматы", "url": "https://api.hh.ru/areas/160"},
            "requirement": "Опыт работы с Django/DRF. - Опыт работы с Redis, Docker, и похожие технологии.",
            "alternate_url": "https://hh.ru/vacancy/107715445",
        },
        {
            "name": "Backend-разработчик",
            "salary": None,
            "area": {"id": "159", "name": "Астана", "url": "https://api.hh.ru/areas/159"},
            "requirement": "Java и Python от 3 лет.Глубокие знания и опыт работы с фреймворками Spring и Django/Flask",
            "alternate_url": "https://hh.ru/vacancy/107653368",
        },
    ]
    return vac
