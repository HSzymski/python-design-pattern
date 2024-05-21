"""
The Singleton design pattern is a creational design pattern that ensures a class has only one instance, and provides a
global point of access to it.
"""


class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance


s1 = Singleton()
s2 = Singleton()
print(s1 is s2)


# Singleton using decorator
def singleton_decorator(class_):
    instances = {}

    def wrapper(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]
    return wrapper


@singleton_decorator
class SomeClass:
    ...
