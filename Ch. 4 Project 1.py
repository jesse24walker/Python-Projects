
plaintext = input("Enter plaintext: ")
distance = int(input("Enter the distance: "))
result = ""

for ch in plaintext:
    result += chr(ord(ch) + distance)

print("\n" + result)
