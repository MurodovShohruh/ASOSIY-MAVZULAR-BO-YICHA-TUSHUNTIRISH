# | Metod         | Vazifasi                         |
# | ------------- | -------------------------------- |
# | `__init__`    | constructor – obyektni yaratish  |
# | `__str__`     | print() uchun matn               |
# | `__repr__`    | texnik representatsiya           |
# | `__len__`     | len() imkoniyati                 |
# | `__add__`     | + operatori                      |
# | `__eq__`      | == operatori                     |
# | `__call__`    | obyektni funksiya kabi chaqirish |
# | `__getitem__` | indekslash                       |
# | `__setitem__` | indeksga qiymat yozish           |

# __init__
# Object yaratilganda avtomatik ishlaydi.
class A:
    def __init__(self, x):
        print("Obyekt yaratildi:", x)
a = A(10)

# __str__
# Obyektni print qilganda chiqariladigan matnni boshqaradi.
class Talaba:
    def __init__(self, ism):
        self.ism = ism
    def __str__(self):
        return f"Talaba: {self.ism}"
t = Talaba("Ali")
print(t)

# __repr__
# Obyektning texnik ifodasini qaytaradi (debug uchun).
class T:
    def __repr__(self):
        return "T() obyekt"

# __len__
# len(obj) ishlashi uchun.
class Box:
    def __init__(self, items):
        self.items = items
    def __len__(self):
        return len(self.items)
b = Box([1,2,3])
print(len(b))   # 3

# __add__
# + operatorini obyektlar uchun belgilaydi.
class Number:
    def __init__(self, x):
        self.x = x
    def __add__(self, other):
        return self.x + other.x
a = Number(3)
b = Number(7)
print(a + b)   # 10

# __eq__
# == solishtirish uchun.
class N:
    def __init__(self, x):
        self.x = x
    def __eq__(self, other):
        return self.x == other.x

# __call__
# Obyektni funksiya kabi chaqirsa bo‘ladi!
class Hello:
    def __call__(self):
        print("Obyekt chaqirildi!")
h = Hello()
h()   # funksiya kabi ishlaydi

# __getitem__
# Obyektni list kabi indekslash imkonini beradi.
class MyList:
    def __init__(self, data):
        self.data = data
    def __getitem__(self, idx):
        return self.data[idx]
ml = MyList([10, 20, 30])
print(ml[1])   # 20

# __setitem__
# Indeksga qiymat yozish.
class MyList:
    def __init__(self):
        self.data = {}
    def __setitem__(self, k, v):
        self.data[k] = v
ml = MyList()
ml["yosh"] = 20
print(ml.data)

# __del__
# Obyekt o‘chirilganda ishlaydi (kam ishlatiladi).
class A:
    def __del__(self):
        print("Obyekt o‘chirildi")

