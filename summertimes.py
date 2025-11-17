print("welcome to the smart coffee machine ")
print("\nMenu")
print("1. Coffee")
print("2. Tea")
print("3. Milk")

choice = input("|nEnter your choice (1/2/3): ")

if choice == "1":
    print("\nPreparing coffee...")
    print("Adding coffee powder, sugar, hot water...")
    print("Your coffee is ready!")

elif choice == "2":
    print("\nPreparing tea...")
    print("Adding tea leaves, milk, sugar...")
    print("Your tea is ready!")

elif choice == "3":
    print("\nPreparing milk...")
    print("Heating the milk...")
    print("Your warm milk is ready!")

else:
    print("\n invalid choice! Please select 1, 2, or 3.")