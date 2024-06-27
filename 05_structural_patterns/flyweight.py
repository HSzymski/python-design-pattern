"""
The Flyweight design pattern is a structural design pattern that allows you to fit more objects into the available
amount of RAM by sharing common parts of state between multiple objects, instead of keeping all of the data in each
object.
"""


class Flyweight:
    def __init__(self, shared_state: str) -> None:
        self._shared_state = shared_state

    def operation(self, unique_state: str) -> None:
        print(f"Flyweight: Displaying shared ({self._shared_state}) and unique ({unique_state}) state.")


class FlyweightFactory:
    _flyweights = {}

    def get_flyweight(self, shared_state: str) -> Flyweight:
        if not self._flyweights.get(shared_state):
            self._flyweights[shared_state] = Flyweight(shared_state)
        return self._flyweights[shared_state]


factory = FlyweightFactory()
flyweight = factory.get_flyweight("shared state")
flyweight.operation("unique state")