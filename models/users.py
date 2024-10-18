from dataclasses import dataclass
from enum import Enum


USER_ADULT_AGE = 18


class Status(Enum):
    student = "student"
    worker = "worker"


@dataclass
class User:
    """Создан абстрактный пользователь с 4 полями"""
    name: str
    age: int
    status: Status
    items: list[str]

    def is_adult(self):
        return self.age >= USER_ADULT_AGE

class Worker(User):

    status = Status.worker

    def __init__(self, name, age, items):
        self.name = name
        self.age = age
        self.items = items


if __name__ == "__main__":
    #     d = {"name": "Oleg",
    #          "age": 16,
    #          "status": "student",
    #          "items": ["book", "pen", "paper"]}

    oleg = User(name="Oleg", age=16, status=Status.student, items=["book", "pen", "paper"])
    olga = User(name="Olga", age=18, status=Status.worker, items=["book", "paper"])
    assert oleg.age == 16, f"Возраст {oleg.name} == {oleg.age}"
    assert olga.age == 18, f"Возраст {olga.name} == {olga.age}"

    """Можем изменять значение экземпляра класса"""
    olga.age += 1
    assert olga.age == 19

    """Благодаря def __eq__(self, other) удается сравнивать между собой экземпляры классов """
    oleg = User(name="Oleg", age=16, status=Status.student, items=["book", "pen", "paper"])
    oleg2 = User(name="Oleg", age=16, status=Status.student, items=["book", "pen", "paper"])
    assert oleg == oleg2

    olga_worker = Worker(name="Olga", age=22, items=["table"])
