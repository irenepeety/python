decimal = int(input("Enter a decimal number: "))

if decimal == 0:
    print("Binary: 0")
else:
    binary = ""
    while decimal > 0:
        binary = str(decimal % 2) + binary
        decimal //= 2

        print("Binary: ", binary)