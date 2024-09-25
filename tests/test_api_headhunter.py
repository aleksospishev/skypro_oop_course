from src.headhunter import HeadHunter


def test_HeadHunter():
    serv1 = HeadHunter()
    assert serv1.url == "https://api.hh.ru/vacancies"
    assert len(serv1.get_vacancies()) == 100
    assert len(serv1.list_vacancies()) == 100

def test_non_valid_HeadHunter():
    serv1 = HeadHunter()
    assert serv1.url == "https://api.hh.ru/vacancies"
    assert len(serv1.get_vacancies()) == 100
    assert len(serv1.list_vacancies()) == 100
