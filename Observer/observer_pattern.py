
"""
Observer Design Pattern
"""

from abc import ABCMeta, abstractclassmethod


class IObservable(metaclass=ABCMeta):
    @staticmethod
    @abstractclassmethod
    def subscribe(observer):
        """The subscribe method"""
        pass

    @staticmethod
    @abstractclassmethod
    def unsubscribe(observer):
        """The unsubscribe method"""
        pass

    @staticmethod
    @abstractclassmethod
    def notify(observer):
        """The notify method"""
        pass


class Subject(IObservable):
    def __init__(self) -> None:
        self._observers = set()

    def subscribe(self, observer):
        self._observers.add(observer)

    def unsubscribe(self, observer):
        self._observers.remove(observer)

    def notify(self, *args, **kwargs):
        for observer in self._observers:
            observer.notify(self, *args, **kwargs)


class IObserver(metaclass=ABCMeta):
    @staticmethod
    @abstractclassmethod
    def notify(observable, *args, **kwargs):
        """Recieve notifications"""
        pass


class Observer(IObserver):
    def __init__(self, observable) -> None:
        observable.subscribe(self)

    def notify(self, observable, *args, **kwargs):
        print("Observer received", args, kwargs)




SUBJECT = Subject()


OBSERVER_A = Observer(SUBJECT)
OBSERVER_B = Observer(SUBJECT)

SUBJECT.notify("Hello Observers", [1,2,3])
SUBJECT.notify("Hello Observers", [1,2,3], {"a":1, "b":2})



