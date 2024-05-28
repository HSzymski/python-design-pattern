"""
The Singleton design pattern is a creational design pattern that ensures a class has only one instance, and provides a
global point of access to it.

Problem of raw Singleton:
- changing values without creating new instance
"""


class SingletonClass:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(SingletonClass, cls).__new__(cls, *args, **kwargs)
        return cls._instance


s1 = SingletonClass()
s2 = SingletonClass()
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


# Singleton using metaclass:

class Singleton(type):  # https://stackoverflow.com/questions/100003/what-are-metaclasses-in-python
    instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.instances:
            cls.instances[cls] = super().__call__(*args, **kwargs)
        return cls.instances[cls]


class Settings(metaclass=Singleton):
    ...