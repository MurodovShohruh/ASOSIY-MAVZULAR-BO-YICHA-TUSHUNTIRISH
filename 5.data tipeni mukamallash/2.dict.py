# Element qo‘shish
talaba={'ism': 'Ali', 'yosh': 20, 'shahar': 'Toshkent'}
talaba["kurs"] = 2   # yangi key-value qo‘shish
print(talaba)

# Element o‘chirish
del talaba["shahar"]   # shahar elementini o‘chiradi
print(talaba)
# Yoki pop():
talaba.pop("yosh")
print(talaba)

# Loop bilan dictda yurish
for k, v in talaba.items():
    print(f"{k} = {v}")
