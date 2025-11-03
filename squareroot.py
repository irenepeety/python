import math

num = float(input("enter a number: "))

if num < 0:
    print("sorry, square root of negative numbers is not defined in real numbers.")
else:
    result = math.sqrt(num)
    print(f"The square root of {num} is {result}")
    