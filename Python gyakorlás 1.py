a = int(input("Befogó: "))
c = int(input("Átfogó: "))
b = (c ** 2 - a ** 2) ** (1/2)
k = a + b + c
t = a * b / 2
print (f"A háromszög kerülete: {k}")
print (f"A háromszög területe: {t}")