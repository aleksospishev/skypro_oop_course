from src.headhunter import HeadHunter
from src.file_manager import JsonFileManager


def action_start(keys_world, path):
    hh_api = HeadHunter()
    hh_vacancies = hh_api.list_vacancies(keys_world)
    saver = JsonFileManager(path)
    saver.write_data(hh_vacancies)
    print(f"Вакансии {keys_world} сохранены в {path}")


def filter_vacancies(vacancies, key_words):
    """Фильтрует список вакансий по ключевым словам в описании."""
    filter_list = []
    for vac in vacancies:
        if key_words.lower() in vac.requirement.lower():
            filter_list.append(vac)
    return sort_vacancies(filter_list)


def sort_vacancies(vacancies):
    """Сортирует список вакансий по убыванию зарплаты."""
    return sorted(vacancies, reverse=True)


def get_top_vacancies(vacancies, n):
    """
    Возвращает верхнюю часть списка вакансий в соответствии с указанным лимитом.
    """
    return sort_vacancies(vacancies)[:n]
