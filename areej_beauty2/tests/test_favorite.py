import pytest
from areej_beauty2.favorite import Favourite  


class DummyCustomer:
    def _init_(self, name):
        self.name = name

@pytest.fixture
def favourite():
    customer = DummyCustomer("Test client")
    return Favourite(customer)

def test_view_favourite_empty(favourite):

    expected = "Your Favourite Products: Your favourite is empty."
    assert favourite.view_favourite() == expected

def test_add_favourite(favourite, capsys):
    
    product_name = "Lipstick"
    favourite.add_favourite(product_name)
    captured = capsys.readouterr().out.strip()
    expected_print = f"{product_name}hes been added to your favourites."
    assert captured == expected_print
    assert product_name in favourite.favourite_items

def test_view_favourite_after_adding(favourite):
    
    products = ["Lipstick", "Foundation"]
    for product in products:
        favourite.add_favourite(product)
    expected = "Your Favourite Products:\n" + "\n".join(products)
    assert favourite.view_favourite() == expected