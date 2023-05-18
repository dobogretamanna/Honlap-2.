l = list(map(lambda x: list(map(int, x.split("!"))), open("input.txt").read().split("\n")))
o = 1
l = l[1]
for i in l:
    o *= i 
print(f"10^{len(str(o)) - 1}")