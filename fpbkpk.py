import math

print("=== FPB & KPK ===")

a = int(input("Masukkan angka pertama: "))
b = int(input("Masukkan angka kedua: "))

fpb = math.gcd(a, b)
kpk = abs(a * b) // fpb

print("FPB:", fpb)
print("KPK:", kpk)