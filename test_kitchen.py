# Test List:
# [x] 200 g * 3 = 600 g
# [x] multiplying a quantity does not modify the original
# [x] two quantities with the same amount and unit are equal
# [x] 1 oz is not the same as 1 g
# [x] 200 g + 300 g = 500 g
# [x] 200 g + 1 oz, reduced to grams, using a conversion rate
# [x] (200 g + 1 oz) * 2

from kitchen import Quantity

def test_multiplication():
    flour = Quantity(200)
    # assert flour.times(3).amount == 600
    assert flour.times(3) == Quantity(600)

def test_multiplication_returns_a_new_quantity():
    flour = Quantity(200)
    # assert flour.times(3).amount == 600
    assert flour.times(3) == Quantity(600)
    # assert flour.times(2).amount == 400
    assert flour.times(2) == Quantity(400)

def test_equality():
    assert Quantity(200) == Quantity(200)
    assert Quantity(200) != Quantity(300)
    