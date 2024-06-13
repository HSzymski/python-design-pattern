"""
The Template Method design pattern is a behavioral design pattern that defines the skeleton of an algorithm in a method,
deferring some steps to subclasses. It lets subclasses redefine certain steps of an algorithm without changing the
algorithm's structure.
"""


class AbstractClass:
    def template_method(self):
        self.base_operation1()
        self.required_operations1()
        self.base_operation2()
        self.hook1()

    def base_operation1(self):
        print("Base operation1")

    def base_operation2(self):
        print("Base operation2")

    def required_operations1(self):
        pass

    def hook1(self):
        pass


class ConcreteClass1(AbstractClass):
    def required_operations1(self):
        print("ConcreteClass1 says: Implemented Operation1")

    def hook1(self):
        print("ConcreteClass1 says: Overridden Hook1")


class ConcreteClass2(AbstractClass):
    def required_operations1(self):
        print("ConcreteClass2 says: Implemented Operation2")


concrete_class = ConcreteClass1()
concrete_class.template_method()