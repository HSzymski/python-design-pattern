"""
* Assignment: DesignPatterns Creational AbstractFactory
* Complexity: easy
* Lines of code: 70 lines
* Time: 21 min

English:
    1. Implement Abstract Factory pattern
    2. Run doctests - all must succeed

Polish:
    1. Zaimplementuj wzorzec Abstract Factory
    2. Uruchom doctesty - wszystkie muszą się powieść

Tests:
    >>> import sys; sys.tracebacklimit = 0
    >>> from pprint import pprint

    >>> main(Platform.iOS)
    iOS Textbox username
    iOS Textbox password
    iOS Button submit

    >>> main(Platform.Android)
    Android Textbox username
    Android Textbox password
    Android Button submit
"""
from dataclasses import dataclass
from abc import ABC, abstractmethod


class ElementFactory(ABC):
    @abstractmethod
    def render(self) -> None:
        raise NotImplementedError


class Button(ElementFactory):
    pass


class Textbox(ElementFactory):
    pass


class OS(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        raise NotImplementedError

    @abstractmethod
    def create_textbox(self) -> Textbox:
        raise NotImplementedError


@dataclass
class ButtonIOS(Button):
    name: str

    def render(self):
        print(f'iOS Button {self.name}')


@dataclass
class ButtonAndroid(Button):
    name: str

    def render(self):
        print(f'Android Button {self.name}')


@dataclass
class TextboxIOS(Textbox):
    name: str

    def render(self):
        print(f'iOS Textbox {self.name}')


@dataclass
class TextboxAndroid(Textbox):
    name: str

    def render(self):
        print(f'Android Textbox {self.name}')


class CreateApp:
    def render(self, platform: Platform):
        platform.create_button().render()
        platform.create_textbox().render()


def main(platform: Platform):
    #TODO: END THAT TASK
    Textbox('username').render(platform)
    Textbox('password').render(platform)
    Button('submit').render(platform)

