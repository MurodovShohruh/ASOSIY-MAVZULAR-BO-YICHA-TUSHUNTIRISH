# LAMBDANING UMUMIY SHAKLI
# lambda argumentlar: ifoda

daraja = lambda x: x ** 2
print(daraja(5))

# Bir nechta argumentli lambda
kopaytir = lambda a, b: a * b
print(kopaytir(3, 4))

# Shart bilan lambda
musbatmi = lambda x: "musbat" if x > 0 else "manfiy"
print(musbatmi(-2))

# Sort ichida ishlatiladigan lambda (eng ko‘p ishlaydi)
names = ["ali", "bekzod", "zokir"]
names.sort(key=lambda x: len(x))
print(names)

# Map + lambda
sonlar = [1, 2, 3, 4]
kv = list(map(lambda x: x**2, sonlar))
print(kv)

# Filter + lambda
sonlar = [1, 2, 3, 4, 5, 6]
juft = list(filter(lambda x: x % 2 == 0, sonlar))
print(juft)

# Lambda + sorted (dict bilan)
talabalar = [
    {"ism": "Ali", "yosh": 20},
    {"ism": "Bek", "yosh": 18},
    {"ism": "Jasur", "yosh": 22}
]
saralash = sorted(talabalar, key=lambda x: x["yosh"])
print(saralash)

# Callback function — Funksiyani boshqa funksiyaga argument sifatida berish
def bajar(func):
    print("Funksiyani ishga tushiryapman...")
    func()
bajar(lambda: print("Salom!"))

# yoki
def hisobla(a, b, oper):
    return oper(a, b)
natija = hisobla(5, 3, lambda x, y: x + y)
print(natija)   # qo‘shish
