import pytest
import os
import json
from areej_beauty2.customer import Customer

@pytest.fixture
def setup_customer_db():
    Customer.Customer_db = 'test_customer_db.json'
    if os.path.exists(Customer.Customer_db):
        os.remove(Customer.Customer_db)

    yield

    if os.path.exists(Customer.Customer_db):
        os.remove(Customer.Customer_db)

def test_register_and_login(setup_customer_db):
    
    customer = Customer.register()
    assert customer is not None
    assert customer.name == "Test User"  
    assert customer.contact == "test@example.com" 
    assert customer.membership == "White"


    logged_in_customer = Customer.login()
    assert logged_in_customer is not None
    assert logged_in_customer.contact == customer.contact

def test_register_existing_account(setup_customer_db):
    Customer.register()
    assert Customer.register() is None 

def test_login_invalid_account(setup_customer_db):
    customer = Customer.login()
    assert customer is None 

def test_logout(setup_customer_db):
    customer = Customer.register()
    assert customer is not None


    result = Customer.logout()
    assert result is None  

