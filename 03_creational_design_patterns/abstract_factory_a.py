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

    >>> main(Platform.IOS)
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
from enum import Enum


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
    def create_button(self, name: str) -> Button:
        raise NotImplementedError

    @abstractmethod
    def create_textbox(self, name: str) -> Textbox:
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


class Android(OS):
    def create_button(self, name: str) -> Button:
        return ButtonAndroid(name)

    def create_textbox(self, name: str) -> Textbox:
        return TextboxAndroid(name)


class IOS(OS):
    def create_button(self, name: str) -> Button:
        return ButtonIOS(name)

    def create_textbox(self, name: str) -> Textbox:
        return TextboxIOS(name)


class Platform(Enum):
    IOS = IOS()
    Android = Android()


def main(platform: Platform):
    os = platform.value
    os.create_textbox('username').render()
    os.create_textbox('password').render()
    os.create_button('submit').render()

