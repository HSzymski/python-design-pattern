"""
The Prototype design pattern is a creational design pattern that allows cloning objects, even complex ones, without
coupling to their specific classes. All prototype classes have a common interface that makes it possible to clone
objects.

Problem:
- Violates Open/Close Principle
"""
import copy


class Prototype:
    def clone(self):
        return copy.deepcopy(self)


class CarPrototype(Prototype):
    pass


car1 = CarPrototype()
car1_copy = car1.clone()
print(car1_copy is not car1)
print(car1_copy == car1)
