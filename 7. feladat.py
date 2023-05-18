l = list(map(lambda x: list(map(int, x.split("!"))), open("input.txt").read().split("\n")))
l = sum(l,[])

paros_szamok = [szam for szam in l if szam % 2 == 0]
paros_szamok_atlag = sum(paros_szamok) / len(paros_szamok)

print("Páros számok átlaga:", paros_szamok_atlag)
