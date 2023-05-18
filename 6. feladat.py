l = list(map(lambda x: list(map(int, x.split("!"))), open("input.txt").read().split("\n")))
lista = l[4]
l[4].sort(reverse=True)
for szam in lista:
    negyzet = szam ** 2
print(negyzet)