"""
The State design pattern is a behavioral design pattern that allows an object to change its behavior when its internal
state changes. This pattern is close to the concept of finite-state machines. The main idea is to declare each possible
state of an object as a separate class and extract all state-specific behaviors into these classes.

The State design pattern has several advantages:
- Flexibility: It provides a way to define a family of behaviors within an object and change the behavior at runtime.
- Encapsulation: Each state is encapsulated in its own class, which makes the code more maintainable and easier to
understand.
- Simplicity: It simplifies the code of the object that changes its behavior. Instead of having many conditional
statements to determine what behavior to execute, the object can simply delegate this to the state object.
- Open/Closed Principle: The State pattern adheres to the Open/Closed Principle as it allows introducing new states
without changing the existing state classes or the context.
- Localizing State-Specific Behavior: Each state class has all the behavior related to a particular state. This makes it
 easier to understand and modify the behavior associated with a particular state.
- State Transitions: State transitions can be explicit and easy to understand because they are triggered by specific
methods in the state classes.
- Reducing State Transition Complexity: The pattern can also reduce the complexity of state transitions because the
decision logic of the transition can be encapsulated within the state classes themselves.

"""

from abc import ABC, abstractmethod


class State(ABC):

    @abstractmethod
    def handle(self, context):
        pass


class ConcreteStateA(State):

    def handle(self, context):
        print("Handling in State A")
        context.state = ConcreteStateB()


class ConcreteStateB(State):

    def handle(self, context):
        print("Handling in State B")
        context.state = ConcreteStateA()


class Context:

    def __init__(self, state: State):
        self._state = state

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state: State):
        self._state = state

    def request(self):
        self._state.handle(self)


if __name__ == '__main__':
    context = Context(ConcreteStateA())
    context.request()

    context.request()

    context.request()
