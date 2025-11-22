# Generator funksiya (yield)
# Katta ma’lumotlarni sekin-sekin qaytaradi.
def count_up_to(n):
    for i in range(n):
        yield i

# Rekursiv funksiya (o‘zini o‘zi chaqiradi)
# Masalan, factorial:
def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

# Ichki funksiya (inner function)
# Funksiya ichida funksiya.
def outer():
    def inner():
        return "Ichki funksiya"
    return inner()

# Callback function (funktsiyani qaytaradigan funksiya)
def outer():
    def inner():
        print("Hello")
    return inner
print(outer())

# Funksiyonlarning ishlashiga ko‘ra bo‘linishi
# | Tur                       | Tavsif                                     |
# | ------------------------- | ------------------------------------------ |
# | **Pure function**         | Tashqi o‘zgaruvchilarga ta’sir qilmaydi    |
# | **Impure function**       | Tashqaridagi o‘zgaruvchilarni o‘zgartiradi |
# | **Higher-order function** | Funksiyani argument sifatida qabul qiladi  |
# | **Anonymous function**    | Nomiz funksiya (lambda)                    |
