# Elementga murojaat qilish (index)
t = ("olma", "banan", "shaftoli")
print(t[0])  # olma
print(t[-1]) # shaftoli

# Tuple uzunligi
t = (1, 2, 3)
print(len(t))  # 3

# Tuple ichida yurish (loop)
fruits = ("olma", "banan", "shaftoli")
for f in fruits:
    print(f)

# Tuple ichida list bo‘lishi mumkin
t = ("olma", [1, 2, 3], "banan")
t[1].append(4)  # list ichini o‘zgartirish mumkin
print(t)

# Tuple unpacking
t = ("Ali", 20, "Toshkent")
name, age, city = t

print(name)  # Ali
print(age)   # 20
print(city)  # Toshkent

