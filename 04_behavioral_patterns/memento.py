"""
The Memento design pattern is a behavioral design pattern that allows an object to save and restore its previous state.
This is useful when you need to provide some sort of undo functionality in your application.
"""


class Memento:
    def __init__(self, state):
        self._state = state

    def get_saved_state(self):
        return self._state


class Originator:
    _state = ""

    def set(self, state):
        print(f"Originator: Setting state to {state}")
        self._state = state

    def save_to_memento(self):
        print("Originator: Saving to Memento.")
        return Memento(self._state)

    def restore_from_memento(self, memento):
        self._state = memento.get_saved_state()
        print(f"Originator: State after restoring from Memento: {self._state}")


class Caretaker:
    def __init__(self):
        self._saved_states = []

    def add_memento(self, memento):
        self._saved_states.append(memento)

    def get_memento(self, index):
        return self._saved_states[index]


if __name__ == "__main__":
    caretaker = Caretaker()
    originator = Originator()

    originator.set('state1')
    originator.set('state2')

    caretaker.add_memento(originator.save_to_memento())

    originator.set('state3')

    caretaker.add_memento(originator.save_to_memento())

    originator.set('state4')

    originator.restore_from_memento(caretaker.get_memento(0))
    originator.restore_from_memento(caretaker.get_memento(1))

