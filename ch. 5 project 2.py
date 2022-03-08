def main():
    
    file = input("Enter the name of the file: ")
    line = []
    with open(file, 'r') as f:
        for line in f:
            line.append(line.strip())

# Splits data into lines
    while True:
        num=int(input("Enter the line number:"))
        if num==0:
            break
    if num <= len(lines):
        print(line[number-1])
    else:
        print("There are not enough line on file")
main()
        
