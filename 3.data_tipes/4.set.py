# SET yaratish
# {} bilan
s = {1, 2, 3, 4}
print(s)

# set() bilan (ro'yxat yoki stringdan)
s2 = set([1, 2, 2, 3, 4])
print(s2)  # takrorlar olib tashlanadi

# 1.add
s = {1, 2, 3}
s.add(4)
print(s)

# 2.remove
s.remove(2)  # 2 ni o‘chiradi, agar bo‘lmasa error

# 3.discard
s.discard(5) # 5 ni o‘chiradi, bo‘lmasa error bermaydi

# SET operatsiyalari (Matematik)
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a.union(b))      # Ikkala setni birlashtiradi {1,2,3,4,5,6}
print(a.intersection(b)) # Kesishma {3,4}
print(a.difference(b))  # Farq {1,2}
print(a.symmetric_difference(b)) # Simmetrik farq {1,2,5,6}
