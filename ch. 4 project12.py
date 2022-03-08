inputFileName = input("Enter file name: ")

print("\n%-15s%-10s%-10s" % ("Name", "Hours", "Total Pay"))
for line in open(inputFileName):
    line = line.strip()

    if line != "":
        (nm, wage, hours) = line.split()

        wage = float(wage)
        hours = int(hours)
        pay = wage * hours

    print("%-15s%-10s%-10.2f" % (nm, hours, pay))
    print(x)
