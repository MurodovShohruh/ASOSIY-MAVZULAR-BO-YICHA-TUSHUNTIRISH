# String kesish (slicing)
s = "Python"
print(s[0:4])  # Pyth (0 dan 4-gacha, 4 kiritilmaydi)
print(s[2:])   # thon (2-indeksdan oxirgacha)
print(s[:3])   # Pyt (boshlashdan 3-indeksgacha)
print(s[-4:-1]) # yth

# | Metod             | Tavsif                                               | Misol                                           |
# | ----------------- | ---------------------------------------------------- | ----------------------------------------------- |
# | `upper()`         | Hammasini katta harfga o‘zgartiradi                  | `"salom".upper()` → `"SALOM"`                   |
# | `lower()`         | Hammasini kichik harfga o‘zgartiradi                 | `"SALOM".lower()` → `"salom"`                   |
# | `strip()`         | Boshlanish va oxirdagi bo‘sh joylarni olib tashlaydi | `"  hello  ".strip()` → `"hello"`               |
# | `replace(a,b)`    | a ni b ga almashtiradi                               | `"salom".replace("s","S")` → `"Salom"`          |
# | `split(sep)`      | Bo‘sh joy yoki sep bo‘yicha bo‘lib beradi            | `"a b c".split()` → `['a','b','c']`             |
# | `join(iterable)`  | Ro‘yxat elementlarini birlashtiradi                  | `" ".join(["salom","dunyo"])` → `"salom dunyo"` |
# | `find(sub)`       | Substring qayerda ekanini topadi, yo‘q bo‘lsa -1     | `"hello".find("l")` → 2                         |
# | `count(sub)`      | Substring necha marta uchrashini hisoblaydi          | `"hello".count("l")` → 2                        |
# | `startswith(sub)` | Substring bilan boshlanadimi                         | `"hello".startswith("he")` → True               |
# | `endswith(sub)`   | Substring bilan tugaydimi                            | `"hello".endswith("lo")` → True                 |


