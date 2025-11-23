# 6. Amaliy misollar
ism = input("Ismingiz: ")
with open("users.txt", "a") as f:
    f.write(ism + "\n")

# 2. Faylni satrma-satr o‘qish
with open("users.txt", "r") as f:
    for satr in f:
        print(satr)

# 3. Faylni tozalab, yangidan yozish
with open("log.txt", "w") as f:
    f.write("Dastur ishga tushdi.\n")
