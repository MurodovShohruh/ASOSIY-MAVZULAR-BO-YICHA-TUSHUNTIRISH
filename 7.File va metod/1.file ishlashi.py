# | Rejim  | Ma’nosi         | Izoh                               |
# | ------ | --------------- | ---------------------------------- |
# | `"r"`  | read            | Faqat o‘qish                       |
# | `"w"`  | write           | Yozish (faylni tozalab yuboradi)   |
# | `"a"`  | append          | Yozish (oxiriga qo‘shadi)          |
# | `"r+"` | o‘qish + yozish | Fayl bor bo‘lishi kerak            |
# | `"w+"` | o‘qish + yozish | Faylni o‘chirib, yangidan yaratadi |
# | `"a+"` | o‘qish + yozish | Oxiridan yozadi                    |

# 1. open() funksiyasi
# open(file_name, mode)

# 2. Faylga yozish — "w"
f = open("data.txt", "w")
f.write("Salom, dunyo!")
f.close()

# 3. Faylga qo‘shish — "a"
f = open("data.txt", "a")
f.write("\nYangi satr qo‘shildi.")
f.close()

# 4. Faylni o‘qish — "r"
f = open("data.txt", "r")
matn = f.read()
print(matn)
f.close()

# readline() — bitta satr o‘qiydi
f = open("data.txt", "r")
print(f.readline())
f.close()

# readlines() — barcha satrlarni list ko‘rinishida o‘qiydi
f = open("data.txt", "r")
print(f.readlines())
f.close()

# 5. Eng to‘g‘ri foydalanish – with open()
# Fayl avtomatik yopiladi
with open("data.txt", "r") as f:
    matn = f.read()
    print(matn)


