n = int(input("Egy egész szám: "))
k = int(input("Egy másik egész szám: "))
def f(z):
    if z == 1:
        return 1
    else:
        return z * f(z - 1)
nf = f(n)
kf = f(k)
nkf = f(n - k)
print (f"A Cnk: {nf // ( kf * nkf)}")
