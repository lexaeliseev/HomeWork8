import csv


def test_workers_are_adult():
    """Тестируем, что все работники  старше 18 лет"""
    with open("users.csv") as csv_file:
        users = csv.DictReader(csv_file, delimiter=";")
        workers = [user for user in users if user["status"] == "worker"]

        # аналогично выше написанному
        # workers = []
        # for user in users:
        #     if user["status"] == "worker":
        #         workers.append(user)

    # в csv dвсе строки str, поэтому переводим в int для сравнения
    for worker in workers:
        assert int(worker["age"]) >= 18, f"Worker {worker['name']} младit 18 лет"

    print()