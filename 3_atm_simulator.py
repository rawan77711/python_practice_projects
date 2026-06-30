"""
atm_simulator.py
A simple ATM simulator program.
"""

PIN=1234  # constant PIN
BALANCE=5000  # starting balance

print("Enter Your PIN:")
entered_pin=int(input())
if entered_pin!=PIN:
    print("Incorrect PIN! The Transaction Was Declined!")
else:
    print("( 1 ) withdraw  ( 2 ) Check Balance")
    operation=int(input("Choose an Option (1 or 2): "))
    if operation==2:
        print(f"Your Current balance is: {BALANCE}")
    elif operation==1:
        print("Enter The Amount to be Withdrawn: ")
        amount=int(input())
        if amount>BALANCE:
            print("Sorry, Your Balance is Insufficient.")
        else:
            print(f"The Operation Was Successful. Your Remaining Balance is: {BALANCE-amount}")
    else:
        print("Incorrect  input!!")
