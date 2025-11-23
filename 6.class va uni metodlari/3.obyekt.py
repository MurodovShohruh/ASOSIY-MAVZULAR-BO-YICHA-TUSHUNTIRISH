# Obyekt nima uchun kerak?
# ✔ Ma’lumotni strukturalash
# ✔ Kodni tartibga solish
# ✔ Ko‘p marta foydalanish
# ✔ Katta loyihalarda boshqaruv oson
# ✔ Real dunyo obyektlarini modellashtirish

# Soddaroq misol
class Phone:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price
p = Phone("Samsung", 250)
print(p.brand)   # Samsung
print(p.price)   # 250

# Objectning o‘z metodlari bo‘ladi
class Student:
    def __init__(self, name, ball):
        self.name = name
        self.ball = ball
    def passed(self):
        return self.ball >= 60
s = Student("Sardor", 75)
print(s.passed())  # True

# 5. Obyektni o‘zgartirish
s.name = "Ulug‘bek"
s.ball = 90


# Obyektga yangi atribut qo‘shish ham mumkin
s.level = "Intermediate"
print(s.level)

