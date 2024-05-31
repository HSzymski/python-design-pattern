"""
The Borg design pattern, also known as the Monostate pattern, is a design pattern that ensures all instances of a class
share the same state. In Python, this is typically implemented using a shared dictionary.
"""


class Borg:
    _shared_state = {}

    def __init__(self):
        # The main use-case for self.__dict__ is when you don't want to access a fixed, known attribute name.
        self.__dict__ = self._shared_state


class ChildBorg(Borg):
    ...


b1 = Borg()
b2 = Borg()
cb3 = ChildBorg()
b1.name = 'Borg'

print(f'''b1 class attr "name": {b1.name}, 
b2 class attr "name": {b2.name}, 
cb2 class attr "name": {cb3.name}''')

print(b1.__dict__)
print(Borg.__dict__)

