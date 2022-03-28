file = input("Enter a file:")
with open(file) as f:
    data = [int(line) for line in f]
print("The average value is", sum(data)/len(data))
