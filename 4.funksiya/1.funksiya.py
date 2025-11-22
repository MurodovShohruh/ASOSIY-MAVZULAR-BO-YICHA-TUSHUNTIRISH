# Funksiya
def funksiya_nomi(argument1, argument2):
    # bajariladigan kod
    natija=argument1+argument2
    return natija

# Oddiy misol
def salom_ber(ism):
    print(f"Salom, {ism}!")
salom_ber("Ali")  # Salom, Ali!
salom_ber("Vali") # Salom, Vali!

# Return bilan qiymat qaytarish
def kvadrat(x):
    return x**2
natija = kvadrat(5)
print(natija)  # 25

# Ko‘p argumentli funksiya
def yigindi(a, b):
    return a + b
print(yigindi(3,5))  # 8

# Return qilmaydigan funksiya
def show():
    print("Hello")
# Faqat bajaradi, None qaytaradi.

# *args — noaniq sonli argumentlar
def summa(*args):
    toplam = 0
    for i in args:
        toplam += i
    return toplam
print(summa(1,2,3,4))  # 10

# **kwargs — kalit so‘zli argumentlar
def salom_ber(**kwargs):
    for k, v in kwargs.items():
        print(f"{k} -> {v}")
salom_ber(ism="Ali", yosh=25, shahar="Toshkent")

