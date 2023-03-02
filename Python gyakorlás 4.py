n = int(input("Egy egész szám: "))
def f(n):
    if n == 1:
        return 1
    else:
        return n * f(n - 1)
print (f"Az egész szám faktorilása: {f(n)}")