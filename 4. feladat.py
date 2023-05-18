l = list(map(lambda x: list(map(int, x.split("!"))), open("input.txt").read().split("\n")))
l[2].sort(reverse=True)
squares = [num**2 for num in l[2][:17]]
total = sum(squares)
print(total)