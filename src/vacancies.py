from src.basic_class import VacancyBasic


class Vacancy(VacancyBasic):
    """Класс вакансии."""

    name: str
    area: dict
    alternate_url: str
    requirement: str
    salary: dict

    __slots__ = ["name", "area", "alternate_url", "requirement", "salary_from", "salary_to"]

    def __init__(self, name, area, alternate_url, requirement, salary=None):
        """Инициализаця класса Vacancy."""
        self.__salary_validation(salary)
        self.name = name
        self.area = area
        self.alternate_url = alternate_url
        self.requirement = requirement

    # @staticmethod
    def __salary_validation(self, salary: dict):
        """Валидация уровня заработной платы."""
        if not salary:
            self.salary_to = 0
            self.salary_from = 0
        else:
            self.salary_to = salary["to"] if salary["to"] else 0
            self.salary_from = salary["from"] if salary["from"] else 0

    def __str__(self):
        """Метод строкого представления экземпляров класса Vacancy."""
        return (
            f"{self.name} \nгород: {self.area['name']}, \n"
            f"заработная плата от {self.salary_from} до {self.salary_to}, \n"
            f"требования {self.requirement}, \n"
            f"ссылка на вакансию {self.alternate_url}. \n"
        )

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.name} {self.area['name']}"

    def __eq__(self, other):
        if isinstance(other, Vacancy):
            return self.salary_from == other.salary_from
        else:
            raise TypeError("Not 'Vacancy' type")

    def __lt__(self, other):
        if isinstance(other, Vacancy):
            return self.salary_from < other.salary_from
        else:
            raise TypeError("Not 'Vacancy' type")

    def __le__(self, other):
        if isinstance(other, Vacancy):
            return self.salary_from <= other.salary_from
        else:
            raise TypeError("Not 'Vacancy' type")

    @classmethod
    def list_vacancies_from_list_dict(cls, vacancies: list[dict]) -> list["Vacancy"]:
        """Возвращает список экземпляров Vacancy из списка словарей."""
        return [cls(**vac) for vac in vacancies]
