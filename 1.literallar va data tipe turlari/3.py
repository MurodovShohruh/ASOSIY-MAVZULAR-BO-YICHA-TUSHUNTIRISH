# 1-usul butun qiymatlar uchun
narx=int(input("narxni kiriting: "))

chegirma=narx-narx*0.15

print(f"Sizning chegirmangiz {chegirma}")

# 2-usul butun bo'lmagan qiymatlar uchun
narx = float(input("Mahsulot narxini kiriting: "))

chegirma = narx * 0.15
yakuniy_narx = narx - chegirma

print(f"Asl narx: {narx}")
print(f"Chegirma: {chegirma}")
print(f"Yakuniy narx: {yakuniy_narx}")
