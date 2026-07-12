"""
Simple Bank Account Management System using Python basics
Features: Register, Login, Deposit, Withdraw, Transfer, Change Password, and Balance Check
"""
#--------------Users Dictionary----------------
users={}

#----------------Register----------------------
def register():
    username=input("Enter username: ").strip()
    password=input("Enter password: ").strip()
    if username == "" or password == "":
        print("Empty input is not allowed!")
        return
    if username in users:
        print("Error: Username already exists.")
        return
    if len(password)<6:
        print("Invalid Password! Password must be at least 6 characters")
        return
    users[username] = {"password":password, "balance":0}
    print(f"Hello {username},Your Account Created Successfully!")

#-----------------Login-------------------------------
def login():
    attempts = 0
    while attempts < 3:
       username=input("Enter username: ").strip()
       password=input("Enter password: ").strip()
       if username not in users:
          print("Error: Username does not exist.")
          attempts+=1
       elif users[username]["password"]!=password:
          print("Error: Incorrect password.")
          attempts+=1
       else:
          print(f"Welcome {username}!\nYour Current Balance: {users[username]['balance']} EGP")
          bank_menu(username)
          return
       print(f"Login failed. Attempts left: {3 - attempts}")
    print("Maximum login attempts reached. Returning to main menu...")
    return None

#-------------------Check Balance----------------------
def checkbalance(username):
     print(f"Your Balance:{users[username]['balance']} EGP")

#-----------------------Deposit------------------------
def deposit(username):
     amount=input("Enter an Amount of Money: ").strip()
     amount=int(amount)
     if amount>0:
         users[username]["balance"]+=amount
         print("Successful Operation!")
         print(f"Receipt: Deposited {amount} EGP\nNew Balance: {users[username]['balance']} EGP")
     elif amount==0:
         print("Operation Cancelled!")
         return
     else:
         print("Invalid Input!!! Amount must be greater than zero")

#-----------------------Withdraw------------------------
def withdraw(username):
    withdraw=input("Enter an Amount of Money to Withdraw: ").strip()
    withdraw=int(withdraw)
    if withdraw<0:
        print("Invalid Input!!! Amount must be greater than zero")
    elif users[username]["balance"]<withdraw:
        print("Insufficient Balance!!")
    elif withdraw==0:
        print("Operation Cancelled!")
        return
    else:
        users[username]["balance"]-=withdraw
        print("Successful Operation!")
        print(f"Receipt: Withdrawn {withdraw} EGP\nNew Balance: {users[username]['balance']} EGP")

#------------------------Transfer-----------------------
def transfer(username):
    recipient=input("Enter recipient name: ").strip()
    if recipient not in users:
        print("Recipient Doesn\'t Exists!!")
        return
    if recipient=="0":
        print("Operation Cancelled!")
        return
    if recipient==username:
        print("You Can\'t Transfer to The Same Account!!")
        return
    amount=input("Enter an Amount of Money to Transfer: ").strip()
    amount=int(amount)
    if amount<0:
        print("Invalid Input!!! Amount must be greater than zero")
    elif users[username]["balance"]<amount:
        print("Insufficient Balance!!")
    elif amount==0:
        print("Operation Cancelled!")
        return
    else:
        users[username]["balance"]-=amount
        users[recipient]["balance"]+=amount
        print("Successful Operation!")
        print(f"Receipt: Transferred {amount} EGP to {recipient}\nYour New Balance: {users[username]['balance']} EGP")

#---------------------Change Password-------------------
def change_password(username):
    current_pass=input("Enter The Current Password: ").strip()
    if current_pass!=users[username]["password"]:
        print("Incorrect Password! Try Again!")
        return
    new_pass=input("Enter New Password: ").strip()
    if len(new_pass)<6:
        print("Invalid Password! Password must be at least 6 characters")
        return
    users[username]["password"]=new_pass
    print("Password Changed Successfully!")


#--------------Bank Menu----------------------
def bank_menu(username):
    while True:
        print("========== Bank Menu ========== ")
        print("1. Check Balance \n2. Deposit \n3. Withdraw \n4. Transfer \n5. Change Password \n6. Logout ")
        menu_choice=int(input("Choose an Option: "))

        if menu_choice==1: 
           checkbalance(username)
        elif menu_choice==2:
           deposit(username)
        elif menu_choice==3:
           withdraw(username)           
        elif menu_choice==4:
           transfer(username)
        elif menu_choice==5:
           change_password(username)
        elif menu_choice==6:
            print("Logging out...")
            break
        else:
            print("Invalid choice!!")

#-------------------------Main-----------------------------
def main():
    while True:
        print("\n========== Welcome To Python Bank ==========")
        print("1. Register \n2. Login \n3. Exit ")
        choice=int(input("Choose an Option: "))
        if choice==1:
            register()
        elif choice==2:
            login()
        elif choice==3:
            print("Thank you for using Python Bank. Goodbye!")
            break
        else:
            print("Invalid Choice!!! Try Again")

#--------------------Run Program----------------------
main()
