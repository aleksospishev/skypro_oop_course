class ConnectionCustomExcept(Exception):
    """Пользовательский класс исключенийб ошибка подключения к серверу"""

    def __init__(self, *args, **kwargs):
        self.message = args[0] if args else "Ошибка подключения к серверу."

    def __str__(self):
        return self.message
