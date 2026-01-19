string = input("PLease enter your own String : ")

string2 = ('')
for i in string:
    string2 = i + string2

print("\nTHe Original String = ", string)
print("The Reversed String = ", string2)