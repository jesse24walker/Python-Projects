from functools import reduce

file = input("Enter file name:")
file = open(file, "r").read().split()
file = list(map(int, file))
print(reduce(lambda x, y: x+y, file, 0)/len(file))
