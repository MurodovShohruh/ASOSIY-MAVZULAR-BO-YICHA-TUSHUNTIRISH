# Setdagi unique elementlar
sonlar = [1, 2, 2, 3, 4, 4, 4, 5]
unique_sonlar = set(sonlar)
print(unique_sonlar)

# Kesishma (intersection) — umumiy elementlar
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
common = A & B
print(common)  # {3, 4}

# Birlashma (union) — barcha elementlar
all_elements = A | B
print(all_elements)  # {1, 2, 3, 4, 5, 6}

# Farq (difference) — A da bor, B da yo‘q
diff = A - B
print(diff)  # {1, 2}

# Loop bilan setda yurish
mevalar = {"olma", "banan", "shaftoli"}

for e in mevalar:
    print(e)
