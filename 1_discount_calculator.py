"""
discount_calculator.py
A simple program to calculate the discount on an amount entered by the user.
"""

print("Welcome To Our Website Sir!")
amount=float(input("Please, Enter The Amount: "))  #The amount value may include fractions
if amount < 100:
    DISCOUNT=0
elif amount < 500:
    DISCOUNT=0.1
else:
    DISCOUNT=0.2
amount_after_discount = amount - (amount * DISCOUNT)
print(
    f"Your Discount is {DISCOUNT * 100:.0f}%, "
    f"and The Amount After Discount is {amount_after_discount:.2f}"
)
print("Thanks For Visiting Our Website, Have a Nice Day!")
