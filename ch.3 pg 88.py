theSum = 0
# Summation with a for loop
for count in range(1, 100001):
    theSum += count
print(theSum)

# Summation with a while loop
theSum = 0
count = 1
while count <= 100000:
    theSum += count
    count += 1
print(theSum)

#Counting down with a for loop

for count in range(10, 0, -1):
    print(count, end = " ")

# Count down with a while loop
count = 10
while count >= 1:
    print(count, end = " ")
    count -= 1
