"""
* Assignment: DesignPatterns Behavioral State
* Complexity: medium
* Lines of code: 34 lines
* Time: 13 min

English:
    1. Implement State pattern
    2. Then add another language:
        a. Chinese hello: 你好
        b. Chinese goodbye: 再见
    3. Run doctests - all must succeed

Polish:
    1. Zaimplementuj wzorzec State
    2. Następnie dodaj nowy język:
        a. Chinese hello: 你好
        b. Chinese goodbye: 再见
    3. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> polish = Translation(Polish())
    >>> english = Translation(English())
    >>> spanish = Translation(Spanish())

    >>> polish.hello()
    'Cześć'
    >>> polish.goodbye()
    'Do widzenia'

    >>> english.hello()
    'Hello'
    >>> english.goodbye()
    'Goodbye'

    >>> spanish.hello()
    'Buenos Dias'
    >>> spanish.goodbye()
    'Adios'
"""
from abc import ABC, abstractmethod


class Language(ABC):
    @abstractmethod
    def hello(self):
        pass

    @abstractmethod
    def goodbye(self):
        pass


class Polish(Language):

    def hello(self):
        return "Cześć"

    def goodbye(self):
        return "Do widzenia"


class English(Language):

    def hello(self):
        return "Hello"

    def goodbye(self):
        return "Goodbye"


class Spanish(Language):

    def hello(self):
        return "Buenos Dias"

    def goodbye(self):
        return "Adios"


class Translation(Language):
    language: Language

    def __init__(self, language: Language):
        self.language = language

    def hello(self):
        return self.language.hello()

    def goodbye(self):
        return self.language.goodbye()

