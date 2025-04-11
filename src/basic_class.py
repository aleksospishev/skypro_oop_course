from abc import ABC, abstractmethod


class APIBasic(ABC):
    @abstractmethod
    def _connect_api(self):
        pass

    @abstractmethod
    def __repr__(self):
        pass

    @abstractmethod
    def get_vacancies(self):
        pass


class VacancyBasic(ABC):
    """Represents a Vacancy"""

    # __slots__ = ('name', 'url', 'salary_from', 'salary_to', 'salary_currency')

    @abstractmethod
    def __eq__(self, other):
        pass

    @abstractmethod
    def __lt__(self, other):
        pass

    @abstractmethod
    def __le__(self, other):
        pass

    @abstractmethod
    def __repr__(self):
        pass


class FileManager(ABC):
    @abstractmethod
    def write_data(self, vacancies):
        pass

    @abstractmethod
    def load_data(self):
        pass

    @abstractmethod
    def delete_data(self):
        pass
