def printAll(seq):
    if seq:
        print("Argument:", seq)
        print(seq[0])
        printAll(seq[1:])


printAll("Jesse")
