import pytest
from areej_beauty2.products import Prodect, ProductManager

@pytest.fixture
def product_manager():
    manager = ProductManager()
    manager.add_product("Lipstick", 150, 20, "Makeup")
    manager.add_product("Foundation", 100, 15, "Makeup")
    manager.add_product("Sunscreen", 99, 0, "Skincare")  # Out of stock product
    return manager

# Test adding a product
def test_add_product(product_manager):
    assert len(product_manager.Prodect) == 3
    product_manager.add_product("Mascara", 120, 10, "Makeup")
    assert len(product_manager.Prodect) == 4

# Test listing products
def test_list_product(product_manager):
    assert "Lipstick" in product_manager.list_product("Makeup")
    assert "Foundation" in product_manager.list_product("Makeup")
    assert "Out of stock" in product_manager.list_product("Skincare")

# Test searching for a product
def test_search_product(product_manager):
    assert "Lipstick" in product_manager.search_product("Lipstick")
    assert "No products found." in product_manager.search_product("Blush")

# Test recommending products
def test_recommend_products(product_manager):
    recommendations = product_manager.recommend_products("Lipstick")
    assert any("Lipstick" in rec for rec in recommendations)
    assert "No recommendation available" in product_manager.recommend_products("Blush")

# Test getting a product by name
def test_get_product(product_manager):
    product = product_manager.get_product("Lipstick")
    assert product is not None
    assert product.name == "Lipstick"
    assert product_manager.get_product("Blush") is None

# Test updating stock
def test_update_stock(product_manager, capsys):
    product_manager.update_stock("Lipstick", 5)
    product = product_manager.get_product("Lipstick")
    assert product.stock == 15
    
    product_manager.update_stock("Lipstick", 20)  # Not enough stock
    captured = capsys.readouterr()
    assert "Not enough stock" in captured.out