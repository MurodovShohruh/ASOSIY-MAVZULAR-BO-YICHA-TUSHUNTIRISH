# | Atribut turi                | Belgisi         | Qayerda ishlatiladi            |
# | --------------------------- | --------------- | ------------------------------ |
# | **Instance attribute**      | `self.x`        | Har bir obyektga alohida       |
# | **Class attribute**         | `ClassName.x`   | Barcha obyektlar uchun umumiy  |
# | **Static attribute/method** | `@staticmethod` | Classga bog‘liq, obyektga emas |
# | **Private attribute**       | `__x`           | Tashqaridan o‘qilmaydi         |
# | **Protected attribute**     | `_x`            | Ichki classlar uchun           |


# 1. Instance attributes (Obyekt atributlari)
# Har bir obyektga alohida tegishli bo‘ladi.
# 👉 __init__() ichida yoziladi.
# 👉 Har bir object o‘ziga xos qiymatga ega bo‘ladi.
class Student:
    def __init__(self, ism, yosh):
        self.ism = ism
        self.yosh = yosh   # instance attribute
s1 = Student("Ali", 20)
s2 = Student("Vali", 25)
print(s1.yosh)  # 20
print(s2.yosh)  # 25


# 2. Class attributes (Classga tegishli atributlar)
# 👉 Barcha obyektlar uchun bir xil qiymatga ega
# 👉 Class ichida, lekin __init__() tashqarisida e’lon qilinadi.
class Student:
    universite = "TATU"  # class attribute
    def __init__(self, ism, yosh):
        self.ism = ism
        self.yosh = yosh
s = Student("Ali", 20)
print(s.universite)      # TATU
print(Student.universite) # TATU


# 3. Static attributes / Static methods
# Class ichida, lekin obyektga aloqasi yo‘q.
# @staticmethod bilan yaratiladi.
# 👉 Obyekt yaratmasdan chaqirilishi mumkin.
class Matematika:
    @staticmethod
    def kvadrat(x):
        return x * x
print(Matematika.kvadrat(5))  # 25


# 4. Private attributes
# __ (ikki pastki chiziq) bilan boshlanadi → tashqaridan o‘qib bo‘lmaydi.
class Bank:
    def __init__(self, balans):
        self.__balans = balans  # private attribute
b = Bank(1000)
# print(b.__balans)  # XATO bo‘ladi


# 5. Protected attributes
# _ (bitta pastki chiziq) bilan boshlanadi → odatda class va ichki meros uchun.
class Animal:
    def __init__(self, name):
        self._name = name   # protected

