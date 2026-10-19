class Quantity:
    def __init__(self, amount, unit):
        self.amount = amount
        self.unit = unit

    def times(self, multiplier):
        return Quantity(self.amount * multiplier, self.unit)

    def plus(self, other):
        return Sum(self, other)
    
    def reduce(self, converter, to_unit):
        rate = converter.rate(self.unit, to_unit)
        return Quantity(self.amount * rate, to_unit)

    def __eq__(self, other):
        return self.amount == other.amount and self.unit == other.unit

    def __repr__(self):
        return f"Quantity({self.amount}, {self.unit!r})"

def grams(amount):
    return Quantity(amount, "g")

def ounces(amount):
    return Quantity(amount, "oz")


class Sum:
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def times(self, multiplier):
        return Sum(self.left.times(multiplier), self.right.times(multiplier))

    def reduce(self, converter, to_unit):
        reduced_left = self.left.reduce(converter, to_unit)
        reduced_right = self.right.reduce(converter, to_unit)
        return Quantity(reduced_left.amount + reduced_right.amount, to_unit)

class Converter:
    def __init__(self):
        self._rates = {}

    def add_rate(self, from_unit, to_unit, rate):
        self._rates[(from_unit, to_unit)] = rate

    def rate(self, from_unit, to_unit):
        if from_unit == to_unit:
            return 1
        return self._rates[(from_unit, to_unit)]

    def reduce(self, source, unit):
        return source.reduce(self, unit)