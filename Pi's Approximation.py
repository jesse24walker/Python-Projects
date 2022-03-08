iteration=int(input("Enter the number of iteration:"))

value=1
c=3

for i in range(iteration-1):
    value=value+(1/c)*((-1)**(i+1))
    c+=2

print("The approximate value of pi is:", value)
