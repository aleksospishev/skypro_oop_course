from utils.utils import filter_vacancies, sort_vacancies, get_top_vacancies


def test_filter_vacancies(vacancy_test_list):
    res = filter_vacancies(vacancy_test_list, "от 2 лет")
    assert res[0].name == 'Senior'


def test_sort_vacansies (vacancy_test_list):
    res = sort_vacancies(vacancy_test_list)
    assert res[2].name == "Backend-разработчик"
    assert res[1].name == "Junior"
    assert res[0].name == "Senior"


def test_get_top_vacancies(vacancy_test_list):
    res = get_top_vacancies(vacancy_test_list, 2)
    assert len(res) == 2
    assert res[0].name == 'Senior'