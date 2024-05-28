"""
The Builder design pattern is a creational design pattern that separates the construction of a complex object from its
representation. It is useful when the construction process must allow different representations for the object that's
constructed.

Problems:
- Violates Open/Close Principle
- Tight coupling between Presentation class with formats
- Duplicated code
"""


class Builder:
    def build_part_a(self):
        pass

    def build_part_b(self):
        pass


class ConcreteBuilder(Builder):
    def build_part_a(self):
        return 'Part A'

    def build_part_b(self):
        return 'Part B'


class Director:
    def __init__(self, builder):
        self.builder = builder

    def construct(self):
        part_a = self.builder.build_part_a()
        part_b = self.builder.build_part_b()
        return part_a, part_b


builder = ConcreteBuilder()
director = Director(builder)
product = director.construct()
print(product)