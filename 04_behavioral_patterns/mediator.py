"""
The Mediator design pattern is a behavioral design pattern that reduces coupling between classes by making them
communicate indirectly, through a mediator object. The mediator object handles and coordinates communication between
different classes.
"""


class Mediator:
    def notify(self, sender, event):
        pass


class ConcreteMediator(Mediator):
    def notify(self, sender, event):
        print(f"Mediator reacting to event: {event}")


class Colleague:
    def __init__(self, mediator):
        self._mediator = mediator

    def do_something(self):
        self._mediator.notify(self, "event")


class ConcreteColleague(Colleague):
    def do_something(self):
        print("Colleague doing something")
        super().do_something()


mediator = ConcreteMediator()
colleague = ConcreteColleague(mediator)

colleague.do_something()
