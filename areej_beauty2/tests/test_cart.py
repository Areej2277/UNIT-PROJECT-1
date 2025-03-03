import pytest
from areej_beauty2.cart import ShoppingCart
from areej_beauty2.products import Prodect

@pytest.fixture
def product():
    return Prodect("Lipstick", 150, 20, "Makeup")

@pytest.fixture
def shopping_cart(product):
    class Customer:
        def _init_(self, name):
            self.name = name
    return ShoppingCart(Customer("Test Customer"))

def test_add_cart(shopping_cart, product):
    shopping_cart.add_cart(product, 2)
    assert product.stock == 18
    assert shopping_cart.cart_item[product.name][1] == 2

def test_add_cart_not_enough_stock(shopping_cart, product):
    shopping_cart.add_cart(product, 25)
    assert product.stock == 18  # Stock should remain the same

def test_remove_cart(shopping_cart, product):
    shopping_cart.add_cart(product, 2)
    shopping_cart.remove_cart(product.name)
    assert product.name not in shopping_cart.cart_item

def test_view_cart(shopping_cart, product, capsys):
    shopping_cart.add_cart(product, 2)
    shopping_cart.view_cart()
    captured = capsys.readouterr()
    assert "Lipstick" in captured.out

def test_checkout(shopping_cart, product, capsys):
    shopping_cart.add_cart(product, 2)
    shopping_cart.checkout()
    captured = capsys.readouterr()
    assert "Your purchase was completed successfully" in captured.out
    assert product.stock == 18  # Ensure stock is updated after checkout