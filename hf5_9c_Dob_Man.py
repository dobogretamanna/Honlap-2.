l = list(map(lambda x: list(map(int, x.split(" "))), open("input.txt").read().split("\n")))
l = l[0]
l.sort()
l2 = ", ".join(list(map(str, l)))
print(l2)

