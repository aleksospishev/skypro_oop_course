import pytest

from src.vacancies import Vacancy


def test_vacancy_init():
    vac = Vacancy("Junior", "Москва", "url1", "Разработка ПО", salary={"from": 20000, "to": 70000})
    assert vac.name == "Junior"
    assert vac.area == "Москва"
    assert vac.alternate_url == "url1"
    assert vac.requirement == "Разработка ПО"
    assert vac.salary_to == 70000
    assert vac.salary_from == 20000


def test_vacancy_list(vacancy_test):
    list_vacancy = Vacancy.list_vacancies_from_list_dict(vacancy_test)
    assert len(list_vacancy) == 2
    assert list_vacancy[0].name == "Strong Junior Backend разработчик"
    assert list_vacancy[0].salary_to == 500000
    assert list_vacancy[1].name == "Backend-разработчик"
    assert list_vacancy[1].salary_from == 0


def test_vacancy_list_none():
    list_vac = Vacancy.list_vacancies_from_list_dict([])
    assert list_vac == []


def test_vacancy_str():
    vac = Vacancy(
        "Junior",
        area={"name": "Москва"},
        alternate_url="url1",
        requirement="Разработка ПО",
        salary={"from": 20000, "to": 70000},
    )
    mes = "Junior \nгород: Москва, \nзаработная плата от 20000 до 70000, \nтребования Разработка ПО, \n" + \
          "ссылка на вакансию url1. \n"

    assert str(vac) == mes
    assert repr(vac) == "Vacancy: Junior Москва"


def test_vacancy_magic(vacancy_test_list):
    assert vacancy_test_list[0] < vacancy_test_list[1]
    assert vacancy_test_list[1] < vacancy_test_list[2]
    with pytest.raises(TypeError):
        vacancy_test_list[2] <= 10000
    with pytest.raises(TypeError):
        vacancy_test_list[2] < 10000


def test_vacancy_eq(vacancy_test_list):
    vac = Vacancy("jun", {"name": "СПб"}, "url4", "pythoт", {"from": 30000, "to": 50000})
    assert vac == vacancy_test_list[1]
    assert vac != vacancy_test_list[2]
    with pytest.raises(TypeError):
        vac == 1
