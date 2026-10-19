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
    flour.times(3)
    assert flour.amount == 600