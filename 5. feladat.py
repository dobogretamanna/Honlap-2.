l = list(map(lambda x: list(map(int, x.split("!"))), open("input.txt").read().split("\n")))
harommal_oszthato = []
for szam in l[3]:
    if szam % 3 == 0:
        harommal_oszthato.append(szam)
legnagyobb = harommal_oszthato[0]
for szam in harommal_oszthato:
    if szam > legnagyobb:
        legnagyobb = szam
print(legnagyobb)
