bill_amount = float(input("Enter the total bill amount: "))
amount_paid = float(input("Enter the amount paid by the customer: "))

if amount_paid < bill_amount:
    due_amount = bill_amount - amount_paid
    print("\nPAyment Status: Incomplete")
    print("Due Amount: $", due_amount)

elif amount_paid > bill_amount:
    change = amount_paid - bill_amount
    print("\nPayment status: overpaid")
    print("Change to return: $", change)

else:
    print("\nPaymeent Status: Paid in Full")
    print("No due amount. Thank you!")


print("\n--- Transaction summary ---")
print("Bill amount: $", bill_amount)
print("amount paid: $", amount_paid)