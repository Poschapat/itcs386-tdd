# test_shipping.py
import pytest
from shipping import shipping_fee


# Rule 1: weight must be more than 0 kg
# BUG 1: Code write `weight_kg < 0` --> 0 kg is not rejected
def test_rule_1_zero_weight_raises_error():
    with pytest.raises(ValueError):
        shipping_fee(0)

def test_rule_1_negative_weight_raises_error():
    with pytest.raises(ValueError):
        shipping_fee(-1)


# Rule 2: up to 1 kg costs 40
# BUG 2: Code write `weight_kg < 1` --> 1 kg to result in 60 instead of 40
@pytest.mark.parametrize("weight, fee", [
    (0.5, 40),   # inside block
    (1, 40),     # up boundary 
])
def test_up_to_one_kg(weight, fee):
    assert shipping_fee(weight) == fee


# Rule 3: more than 1 kg and up to 5 kg costs 60
@pytest.mark.parametrize("weight, fee", [
    (1.1, 60),   # down boundary
    (3, 60),     # inside block
    (5, 60),     # up boundary
])
def test_between_one_and_five_kg(weight, fee):
    assert shipping_fee(weight) == fee


# Rule 4: more than 5 kg = 60 + 10 per started kg above 5
# BUG 3: Code write `int()` --> round down, need to round up (5.2 kg gets 60 instead of 70)
@pytest.mark.parametrize("weight, fee", [
    (5.1, 70),   
    (5.2, 70),     # breaks when code uses int() truncating instead of ceiling
    (6, 70),       # exactly 1 kg above 5
    (6.5, 80),     # partial kg above 6
    (7, 80),      
])
def test_above_five_kg(weight, fee):
    assert shipping_fee(weight) == fee