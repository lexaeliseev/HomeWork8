import pytest
import csv
from models.users import User

"""Используем объектный подход в работе с данными"""
"""Создана директория models с файлом users (class Users)"""

@pytest.fixture
def users() -> list[User]:
    """Читаем файл и записываем результат в список"""
    with open("users.csv") as csv_file:
        users = list(csv.DictReader(csv_file, delimiter=";"))
    return [User(name=user["name"],
                 age=int(user["age"]),
                 status=user["status"],
                 items=user["items"])
            for user in users]


@pytest.fixture()
def workers(users) -> list[User]:
    """Берем только работников из списка пользователей"""
    workers_value = [user for user in users if user.status == "worker"]
    return workers_value
    # Аналогично выше написанному
    # workers = []
    # for user in users:
    #     if user["status"] == "worker":
    #         workers.append(user)
    # return workers_value


def test_workers_are_adult_v2(workers):
    """Тестируем, что все работники  старше 18 лет из csv файла"""
    for worker in workers:
        assert user_is_adult(worker), f"Worker {worker.name} младше 18 лет"


def user_is_adult(user: User):
    """Выносим в отдельную функцию преобразование типа данных и сравнение возраста"""
    return user.age >= 18