new = int(input("Enter the amount of new videos per night:"))
oldie = int(input("Enter the amount of old videos per night:"))
totalCost = 3 * new + 2 * oldie
print("The total cost of records rented per night is", '$' + str(totalCost))
