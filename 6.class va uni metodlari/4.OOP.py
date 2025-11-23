# OOP turlari (prinsiplari) qisqacha:
# | Prinsip           | Ma’nosi                                  |
# | ----------------- | ---------------------------------------- |
# | **Encapsulation** | Ma’lumotni yashirish, himoyalash         |
# | **Inheritance**   | Mavjud classdan yangi class yaratish     |
# | **Polymorphism**  | Bir xil nomli metodlar turlicha ishlashi |
# | **Abstraction**   | Keraksiz detallarni yashirish            |


# 1. Encapsulation (Inkapsulyatsiya)
# Ma’lumotni yashirish va himoyalash.
# 👉 Obyektning ichki ma’lumotlari tashqaridan to‘g‘ridan-to‘g‘ri o‘zgartirilmaydi.
# 👉 Faqat metodlar orqali boshqariladi.
class Bank:
    def __init__(self, balans):
        self.__balans = balans   # private attribute

    def get_balans(self):
        return self.__balans

    def depozit(self, summa):
        self.__balans += summa

bank = Bank(1000)
bank.depozit(500)
print(bank.get_balans())   # 1500


# 2. Inheritance (Meros olish)
# Bitta class boshqa classning xususiyatlarini meros qilib oladi.
# 👉 Kodni qayta yozmaslik uchun.
# 👉 Har bir child class, parent classdan metod va atributlarni oladi.
class Hayvon:
    def ovoz(self):
        print("Hayvon ovoz chiqaryapti")

class It(Hayvon):
    def ovoz(self):
        print("Vov-vov")

dog = It()
dog.ovoz()  # Vov-vov


# 3. Polymorphism (Polimorfizm)
# Bitta metod turlicha ishlaydi (har bir classda o‘ziga xos bo‘ladi).
class Quyon:
    def ovoz(self):
        print("...")

class Mushuk:
    def ovoz(self):
        print("Meow")

class It:
    def ovoz(self):
        print("Vov")

for animal in (Quyon(), Mushuk(), It()):
    animal.ovoz()

# 4. Abstraction (Abstraksiyalar)
# Foydalanuvchi faqat kerakli qismini ko‘radi, murakkab jarayonlar yashiriladi.
# 👉 OOP’dagi “faqat zarur funksiyani ko‘rsatish”.
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Kvadrat(Shape):
    def __init__(self, a):
        self.a = a

    def area(self):
        return self.a * self.a

k = Kvadrat(4)
print(k.area())  # 16
