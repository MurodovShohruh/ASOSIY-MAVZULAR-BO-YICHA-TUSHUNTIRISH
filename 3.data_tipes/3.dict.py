# # 1. get
d = {"ism": "Ali", "yosh": 20}
print(d.get("ism"))        # Ali
print(d.get("manzil"))     # None
print(d.get("manzil", "yo‘q"))  # yo‘q

# 10. setdefault
d = {"ism":"Ali"}
d.setdefault("yosh", 20)
print(d)

# DICTIONARY YARATISH
d = {
    "ism": "Ali",
    "yosh": 20,
    "shahar": "Toshkent"
}

# ELEMENT QO‘SHISH
d["kasb"] = "dasturchi"

# ELEMENTNI O‘ZGARTIRISH
d["yosh"] = 21

# ELEMENT BOR-YO‘QLIGINI TEKSHIRISH
if "ism" in d:
    print("Bor")

# Dictionaryni to‘liq listga aylantirish (kalit + qiymat)
d = {"a":1, "b":2, "c":3}

lst = []
for k, v in d.items():
    lst.append(k)
    lst.append(v)

print(lst)

# List comprehension yordamida
lst = [v for v in d.values()]
print(lst)

# Ikki listdan dict yaratish (zip bilan)
keys = ["ism", "yosh", "shahar"]
values = ["Ali", 25, "Toshkent"]

d = {k: v for k, v in zip(keys, values)}
print(d)

# Range orqali avtomatik dict yaratish
d = {x: x**2 for x in range(1, 6)}
print(d)
