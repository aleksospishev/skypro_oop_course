from src.file_manager import JsonFileManager
from src.vacancies import Vacancy
from utils.utils import action_start, sort_vacancies, get_top_vacancies, filter_vacancies

path = "./data/data.json"


def my_proj():
    keys_world = input("Введите ключевые слова для поиска вакансий\n")
    action_start(keys_world, path)
    flag = True
    while flag:
        action_second = int(
            input(
                """Для вывода всех вакансий введите 1
Для вывода лучших вакансий по уровню з.п. введите 2
Для поиска вакансий по ключевому слову введите 3\n"""
            )
        )
        if action_second in (1, 2, 3):
            file = JsonFileManager(path)
            list_vacancy = file.load_data()
            if action_second == 1:
                list_vacancy = sort_vacancies(list_vacancy)
            elif action_second == 2:
                count_vacancies = int(input("Введите кол-во интересуемых вакансий.\n"))
                list_vacancy = get_top_vacancies(list_vacancy, count_vacancies)
            else:
                key_search = input("Введите ключевые слова для поиска\n").split()
                list_vacancy = filter_vacancies(list_vacancy, key_search)
            if len(list_vacancy) == 0:
                print("По вашему вопросу нет подходящих Вакансий.")
            for el in list_vacancy:
                print(el)
            flag = False
        else:
            print("Вы выбрали неверное действие.")


if __name__ == "__main__":
    print("Добро пожаловать! Помогу вам выбрать подходящие вакансии!")
    my_proj()
    print("До скорых встреч!")

