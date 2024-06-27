"""
The Facade design pattern is a structural design pattern that provides a simplified interface to a complex subsystem.
It provides a unified interface to a set of interfaces in a subsystem, which makes the subsystem easier to use.
"""


class Subsystem1:
    def operation1(self) -> str:
        return "Subsystem1: Ready!\n"


class Subsystem2:
    def operation2(self) -> str:
        return "Subsystem2: Go!\n"


class Facade:
    def __init__(self, subsystem1: Subsystem1, subsystem2: Subsystem2) -> None:
        self._subsystem1 = subsystem1
        self._subsystem2 = subsystem2

    def operation(self) -> str:
        results = []
        results.append("Facade initializes subsystems:\n")
        results.append(self._subsystem1.operation1())
        results.append(self._subsystem2.operation2())
        return "".join(results)


subsystem1 = Subsystem1()
subsystem2 = Subsystem2()
facade = Facade(subsystem1, subsystem2)
print(facade.operation())

