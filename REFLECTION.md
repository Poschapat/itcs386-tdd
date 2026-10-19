# Part B: Reflection

### 1. How many tests did you write in Part A, and how many lines of production code? What is the ratio?
In Part A, we wrote 8 test functions in `test_kitchen.py` (covering multiplication, value object immutability, equality, unit distinction, simple addition, mixed units addition, rate direction, and sum multiplication). In `kitchen.py`, there are approximately 50 lines of production code. The ratio of test code to production code is approximately 1:1, showing that testing logic comprises an equal and essential portion of development alongside implementation.

### 2. When was your bar red for the longest time, and what made it last so long?
The bar stayed red the longest during Step A7 (Mixed units and conversion rates). This was because it required an architectural refactoring: changing the signature of `reduce` across `Quantity`, `Sum`, and `Converter` to pass the `converter` context instance down into the composite expression tree, rather than simply writing a straightforward return formula.

### 3. Find one place where you used Fake It, one where you triangulated, and one where you used Obvious Implementation. Looking back, was each choice right?
- **Fake It:** Used in Step A1 where `self.amount = 600` was hard-coded. This was the right choice because it quickly verified the test infrastructure without worrying about design.
- **Triangulate:** Used in Step A2 by adding `test_multiplication_by_two()` to force the generalization from a hardcoded 600 to `self.amount * multiplier`. It helped prevent premature generalization.
- **Obvious Implementation:** Used in Step A8 when adding `times()` to `Sum`, distributing the multiplier to `self.left.times(multiplier)` and `self.right.times(multiplier)`. Because the Composite pattern was already well established, the implementation was obvious and safe.

### 4. Which items are still on your test list? Which would you implement next, and which should you delete because they were speculation?
- **Items remaining:** Subtraction (`Quantity.minus`), handling division, and implementing `__hash__` so quantities can be used in dictionaries/sets.
- **Next to implement:** Subtraction (`200 g - 50 g`), as it is a natural counterpart to addition and reuses the existing `reduce` design.
- **To delete:** Complex conversions between non-linear units (e.g., Celsius to Fahrenheit) or currency conversions, as they add speculative complexity unnecessary for simple recipe ingredient tracking.

### 5. Look at Quantity.reduce. If you had designed the whole system on paper first, would you have written this method?
Probably not. In a traditional upfront paper design, one would likely have placed all conversion logic inside `Converter` by extracting amounts and units procedurally (e.g., using `isinstance`). TDD naturally drove the polymorphic `reduce` method down into `Quantity` and `Sum` so they can evaluate themselves uniformly, leading to the Composite pattern cleanly.

### 6. In Part 0 you wrote the tests after the code, and in Part A before it. How did the two feel different, and which tests shaped your design?
Writing tests after code in Part 0 felt like a verification chore where we adhered to preexisting functions and docstrings. In contrast, writing tests first in Part A drove API design from the client's perspective. Specifically, `test_equality()` demanded value-object behavior, and `test_simple_addition()` forced the creation of deferred evaluation expressions (`Sum`), directly shaping the architecture before implementation.