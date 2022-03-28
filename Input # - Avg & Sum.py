theSum = 0.0

i = 0

# Loops until enter
while True:
    data = input("Enter a number or press Enter to quit: ")

# If user pressed enter
    if data == '':
        break
    number = float(data)
    theSum += number

# Increases the number of terms
    i += 1
print()
print("The sum is", theSum)

# if entered numbers are greater tahn 0
if i > 0:

    # Average
    average = theSum / i
    print("The average is", average)

# if nothing is entered
else:
    print("Average : undefined (as the number of terms entered are 0)")
