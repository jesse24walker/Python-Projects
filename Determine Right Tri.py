
side1 = int(input("Enter the first side of the triangle: "))
side2 = int(input("Enter the second side of the triangle: "))
side3 = int(input("Enter the third side of the traingle: "))

#Pythagorean theorem for a right triangle
if (side1 ** 2 + side2 ** 2) == side3 ** 2 or (side3 ** 2 + side2 ** 2) == side1 ** 2 or (side1 ** 2 + side3 ** 2) == side2 ** 2:
    print("This is a right triangle")
else:
    print("This is not a right triangle")
