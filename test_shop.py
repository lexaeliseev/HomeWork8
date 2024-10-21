"""
Протестируйте классы из модуля models.py
"""
import pytest

from models import Product


@pytest.fixture
def product():
    return Product("book", 100, "This is a book", 1000)


class TestProducts:
    """
    Тестовый класс - это способ группировки ваших тестов по какой-то тематике
    Например, текущий класс группирует тесты на класс Product
    """

    def test_product_check_quantity(self, product):
        # TODO напишите проверки на метод check_quantity
        assert product.check_quantity(1) is True, f"Ошибка! Количество товаров равно = {product.quantity}"
        assert product.check_quantity(1000) is True, f"Ошибка! Количество товаров равно = {product.quantity}"
        assert product.check_quantity(1001) is False, f"Ошибка! Количество товаров равно = {product.quantity}"

    def test_product_buy(self, product):
        # TODO напишите проверки на метод buy
        product.buy(100)
        assert product.quantity == 900, f"Ошибка! Количество товаров равно = {product.quantity}"

        product.buy(200)
        assert product.quantity == 700, f"Ошибка! Количество товаров равно = {product.quantity}"

        product.buy(700)
        assert product.quantity == 0, f"Ошибка! Количество товаров равно = {product.quantity}"

    def test_product_buy_more_than_available(self, product):
        # TODO напишите проверки на метод buy,
        #  которые ожидают ошибку ValueError при попытке купить больше, чем есть в наличии
        with pytest.raises(ValueError, match='Не хватает товаров на складе!'):
            product.buy(1001)


#
# class TestCart:
#     """
#     TODO Напишите тесты на методы класса Cart
#         На каждый метод у вас должен получиться отдельный тест
#         На некоторые методы у вас может быть несколько тестов.
#         Например, негативные тесты, ожидающие ошибку (используйте pytest.raises, чтобы проверить это)
#     """
