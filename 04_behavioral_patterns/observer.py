"""
The Observer design pattern is a behavioral design pattern that allows an object (known as the subject) to notify other
objects (known as observers) about changes in its state. The subject maintains a list of observers and provides methods
to add and remove observers from this list. When the state of the subject changes, it sends a notification to all its
observers. This pattern is particularly useful in event-driven programming.
"""
from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, message):
        pass


class ToBeNotified(Observer):

    def update(self, message):
        print(f'ToBeNotified class received {message}')


class Subject:

    def __init__(self):
        self.observers_list = []

    def register(self, observer: Observer):
        self.observers_list.append(observer)

    def unregister(self, observer: Observer):
        self.observers_list.remove(observer)

    def notify(self, message):
        for observer in self.observers_list:
            observer.update(message)


subject = Subject()
class_to_be_notified = ToBeNotified()
subject.register(class_to_be_notified)
subject.notify('"Seal of approval"')
