from dataclasses import dataclass


@dataclass
class User:
    """Создан абстрактный пользователь с 4 полями"""
    name: str
    age: int
    status: str
    items: list[str]

    """Если используем dataclass, то def __init__(self, name, age, status, items) не нужен"""
    # def __init__(self, name, age, status, items):
    #     self.name = name
    #     self.age = age
    #     self.status = status
    #     self.items = items

    """__eq__ это функция, которая вызывается в момент сравнения одного экземпляра класса с другим и возвращает bool"""
    """Если используем dataclass, то def __init__(self, name, age, status, items) не нужен"""

    # def __eq__(self, other):
    #     return (self.name == other.name and
    #             self.age == other.age and
    #             self.status == other.status and
    #             self.items == other.items)


if __name__ == "__main__":
    #     d = {"name": "Oleg",
    #          "age": 16,
    #          "status": "student",
    #          "items": ["book", "pen", "paper"]}

    oleg = User(name="Oleg", age=16, status="student", items=["book", "pen", "paper"])
    olga = User(name="Olga", age=18, status="worker", items=["book", "paper"])
    assert oleg.age == 16, f"Возраст {oleg.name} == {oleg.age}"
    assert olga.age == 18, f"Возраст {olga.name} == {olga.age}"

    """Можем изменять значение экземпляра класса"""
    olga.age += 1
    assert olga.age == 19

    """Благодаря def __eq__(self, other) удается сравнивать между собой экземпляры классов """
    oleg = User(name="Oleg", age=16, status="student", items=["book", "pen", "paper"])
    oleg2 = User(name="Oleg", age=16, status="student", items=["book", "pen", "paper"])
    assert oleg == oleg2
