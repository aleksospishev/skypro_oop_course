# HeadHunter vacancy

## Описание

Программа для получения информации о вакансиях с платформы api.hh.ru
Проект состоит из пакета: src, содержащий модули:
- basic_class описывающий все родительские классы используемые в проекте
- headhunter класс наследованный от APIBasic, реализован для подключения к "https://api.hh.ru/vacancies"
получение всех вакансий в виде списка json через метод 'get_vacancies',
получение списка вакансий в формате словаря с ключами (name, salary, area, requirement, alternate_url) 
- vacancies класс наследованный от VacancyBasic, экземпляры класса имеют атрибуты:
  name: str 
  area: dict
  alternate_url: str
  requirement: str
  salary: dict
атрибут salary имеет внутреннию валидацию через метод __salary_validation
экземпляры класса имеют методы сравнения __le__, __qe__, __lt__
реализованы методы текстового представления экземпляров __repr__ и __str__
реализован классовый метод list_vacancies_from_list_dict; возвращающий список экземпляров класса из списка словарей
  - file_manager содержит методы write_data записи в файл Json списка вакансий, 
  load_data для выгрузки данных из файла json в список вакансий
  delete_data для очистки файла от данных

## Технологии
- [Python 3.12]
- [ООП]
- [Poetry]
- [Pytest]
- [JSON]
- [Request]
- [API]

## Тестирование
Проект покрыт тестами на 80%

## Установка 

1. Клонируйте репозиторий:
```
git clone https://github.com/aleksospishev/sky_shop.git
```

2. Установите зависимости:
```
poetry install
```
3. Запуск тестов:
```
poetry pytest
```
4. Проверить покрытие кода тестами
```
poetry run pytest --cov
```

