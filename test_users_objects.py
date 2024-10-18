import pytest
import csv

from models.providers import UserProvider, CsvUserProvider, DataBaseUserProvider, ApiUserProvider
from models.users import User, USER_ADULT_AGE, Status, Worker

"""Используем объектный подход в работе с данными"""
"""Создана директория models с файлом users (class Users)"""


@pytest.fixture(params=[CsvUserProvider, DataBaseUserProvider, ApiUserProvider])
def user_provider(request) -> UserProvider:
    return request.param()

@pytest.fixture
def users(user_provider) -> list[User]:
    return user_provider.get_users()


@pytest.fixture()
def workers(users) -> list[Worker]:
    """Берем только работников из списка пользователей"""
    workers_value = [Worker(name=user.name, age=user.age, items=user.items)
                     for user in users if user.status == Status.worker]
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
        assert worker.is_adult, f"Worker {worker} младше {USER_ADULT_AGE} лет"


def user_is_adult(user: User):
    """Выносим в отдельную функцию преобразование типа данных и сравнение возраста"""
    return user.age >= USER_ADULT_AGE