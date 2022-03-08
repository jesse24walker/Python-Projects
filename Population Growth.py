organisms=int(input("Enter the initial number of organisms:"))
growthRate=int(input("Enter the rate of growth:"))
hoursForRate=int(input("Enter the number of hours it takes to achieve this rate:"))
hoursForGrowth=int(input("Enter the number of hours during which the population grows:"))

while hoursForRate <= hoursForGrowth:
    organisms*=growthRate
    hoursForRate+=hoursForRate

print("The total population is", organisms)
