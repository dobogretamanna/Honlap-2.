l = list(map(lambda x: list(map(int, x.split("!"))), open("input.txt").read().split("\n")))
o = 0
l = l[0]
for i in l:
    o += i if i < 24 else 0
print(o)