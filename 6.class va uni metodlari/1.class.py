# . Oddiy Class (Basic Class)
# Eng ko‘p ishlatiladigani.
class Person:
    def __init__(self, name):
        self.name = name
p = Person("Ali")

# Inheritance Class (Meros olish)
# Bitta class boshqasidan xususiyat oladi.
class Animal:
    def speak(self):
        print("Some sound")
class Dog(Animal):
    def speak(self):
        print("Woof!")

# Multiple Inheritance (Ko‘p meros)
# Class bir nechta classdan meros oladi.
class A:
    pass
class B:
    pass
class C(A, B):
    pass

# Abstract Class (Abstrakt class)
# Faol bo‘lmaydi, faqat skeleton (shablon) beradi.
from abc import ABC, abstractmethod
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

# Staticmethod Class / Utility Class
# Faqat staticmethod va classmethod ishlatiladi.
class Math:
    @staticmethod
    def add(a,b):
        return a+b

# Singleton Class
# Faqat bitta obyekt yarata oladigan class.
class Singleton:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

# Dataclass
# Ma’lumot saqlash uchun qulay class (Python 3.7+)
from dataclasses import dataclass
@dataclass
class User:
    name: str
    age: int

# Nested Class (Ichki Class)
# Class ichida class.
class A:
    class B:
        pass

# Enum Class
# O‘zgarmas qiymatlar to‘plami.
from enum import Enum
class Color(Enum):
    RED = 1
    BLUE = 2

# Mixins Class
# Qo‘shimcha funksionallik beruvchi class (faqat meros uchun).
class LogMixin:
    def log(self):
        print("Logged!")
class User(LogMixin):
    pass

