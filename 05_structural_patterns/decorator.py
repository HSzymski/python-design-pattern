"""
The Decorator design pattern is a structural design pattern that allows behavior to be added to an individual object,
either statically or dynamically, without affecting the behavior of other objects from the same class.
"""


class Component:
    def operation(self) -> str:
        return "Component"


class Decorator(Component):
    _component: Component = None

    def __init__(self, component: Component) -> None:
        self._component = component

    def operation(self) -> str:
        return self._component.operation()


class ConcreteDecoratorA(Decorator):
    def operation(self) -> str:
        return f"ConcreteDecoratorA({self._component.operation()})"


class ConcreteDecoratorB(Decorator):
    def operation(self) -> str:
        return f"ConcreteDecoratorB({self._component.operation()})"


simple = Component()
decorator1 = ConcreteDecoratorA(simple)
decorator2 = ConcreteDecoratorB(decorator1)
print(decorator2.operation())