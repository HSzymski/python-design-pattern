"""
The Composite design pattern is a structural design pattern that allows you to compose objects into a tree structure
and work with these objects as if they were individual objects. This pattern is particularly useful when dealing with
a hierarchy of objects.
"""

from abc import ABC, abstractmethod


class Component(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass


class Leaf(Component):
    def operation(self) -> str:
        return "Leaf"


class Composite(Component):
    def __init__(self) -> None:
        self._children = []

    def add(self, component: Component) -> None:
        self._children.append(component)

    def remove(self, component: Component) -> None:
        self._children.remove(component)

    def operation(self) -> str:
        results = []
        for child in self._children:
            results.append(child.operation())
        return f"Branch({'+'.join(results)})"


simple = Leaf()
print(simple.operation())

tree = Composite()
tree.add(simple)
branch = Composite()
branch.add(Leaf())
branch.add(Leaf())
tree.add(branch)
print(tree.operation())
