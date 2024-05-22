"""
The Abstract Factory design pattern is a creational design pattern that provides an interface for creating families of
related or dependent objects without specifying their concrete classes.
"""


class AbstractFactory:
    def create_product_a(self):
        pass

    def create_product_b(self):
        pass


class ConcreteFactory1(AbstractFactory):
    def create_product_a(self):
        return ConcreteProductA1()

    def create_product_b(self):
        return ConcreteProductB1()


class ConcreteFactory2(AbstractFactory):
    def create_product_a(self):
        return ConcreteProductA2()

    def create_product_b(self):
        return ConcreteProductB2()


class AbstractProductA:
    pass


class ConcreteProductA1(AbstractProductA):
    pass


class ConcreteProductA2(AbstractProductA):
    pass


class AbstractProductB:
    pass


class ConcreteProductB1(AbstractProductB):
    pass


class ConcreteProductB2(AbstractProductB):
    pass


factory1 = ConcreteFactory1()
product_a1 = factory1.create_product_a()
product_b1 = factory1.create_product_b()
factory2 = ConcreteFactory2()
product_a2 = factory2.create_product_a()
product_b2 = factory2.create_product_b()
