# 1. Modul nima?
# Modul — bu alohida Python fayli yoki kutubxona bo‘lib, ichida funksiyalar, klasslar va o‘zgaruvchilar saqlanadi.
# Biz modulni import qilib, ichidagi funksiyalardan foydalanamiz.

# import turlari
# 1. Oddiy import
import math

# 2. Moduldan bitta funksiya olish
from math import sqrt

# 3. Modulni qisqa nom bilan chaqirish
import datetime as dt

# O‘z modulimizni yaratish
# masalan, my_module.py degan fayl ochamiz:
def salom():
    return "Salom dunyo!"
def kvadrat(x):
    return x * x
# boshqa faylda import qilamiz:
# import my_module
# print(my_module.salom())
# print(my_module.kvadrat(5))

