char = input("Enter a character: ")

if len(char) == 1:
    if char.isalpha():
        print("It is an alphabtet.")
    else:
        print("It is NOT an alphabet.")
else:
    print("Please enter only one character!")