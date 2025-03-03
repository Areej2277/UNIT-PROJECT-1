import pytest
from areej_beauty2.membership import Membership   

@pytest.fixture
def membership():
    return Membership("Gold")   

def test_add_points(membership):
    membership.add_points(100)
    assert membership.loyalty_points == 100

def test_redeem_points_success(membership):
    membership.add_points(50)
    success = membership.redeem_points(30)
    assert success is True
    assert membership.loyalty_points == 20 

def test_redeem_points_failure(membership):
    membership.add_points(20)
    success = membership.redeem_points(30)
    assert success is False  
    assert membership.loyalty_points == 20  

def test_str(membership):
    membership.add_points(50)
    assert str(membership) == "Membership Type: Gold, Loyalty Points: 50"     