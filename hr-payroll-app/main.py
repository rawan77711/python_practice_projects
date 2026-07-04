"""
Simple HR Payroll Application.
This program calculates an employee's bonus, tax, and net salary
based on their base salary and performance rating.
"""

def calculate_bonus(base_salary, performance_rating):
    """Calculate bonus amount based on base salary and performance rating."""
    if performance_rating==5:
        bonus_amount=0.2
    elif performance_rating in (3,4):
        bonus_amount=0.1
    else:
        bonus_amount=0
    return bonus_amount*base_salary

def  calculate_tax(gross_salary):
    """Calculate tax amount based on gross salary."""
    if gross_salary>7000:
        tax_amount=0.15
    elif gross_salary>=3000:
        tax_amount=0.1
    else:
        tax_amount=0
    return tax_amount*gross_salary

def main_hr_app():
    """Run the HR payroll application: input, validation, and output."""
    print("="*40)
    print("--- Corporate Payroll System ---")
    print("="*40)

    #User Input:
    employee_name=input("Enter Employee Name: ").strip().capitalize()
    department=input("Enter Department Name: ").strip()
    base_salary=float(input("Enter Base Salary: "))
    performance_rating=int(input("Enter Performance Rating (1-5): "))

    #Validation:
    if performance_rating<1 or performance_rating>5 or base_salary<0:
        print("Invalid Input!!")
        print("Please Try Again!!")
        return

    #Calculations:    
    bonus=calculate_bonus(base_salary,performance_rating)
    gross_salary=base_salary+bonus
    tax=calculate_tax(gross_salary)
    net_salary=gross_salary-tax
    
    #Output:
    print("="*40)
    print(f" Payroll Statement For: {employee_name}")
    print("="*40)
    print(f"Base Salary      :  {base_salary:,.2f} EGP")
    print(f"Earned Bonus     :  {bonus:,.2f} EGP")
    print(f"Gross Salary     :  {gross_salary:,.2f} EGP")
    print(f"Tax Deductions   :  {tax:,.2f} EGP")
    print("-"*40)
    print(f"NET PAYABLE CASH :  {net_salary:.2f} EGP")
    print("="*40+"\n")

main_hr_app()
