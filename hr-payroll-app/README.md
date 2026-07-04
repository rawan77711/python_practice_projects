# 💼 HR Payroll Application
A simple command-line Python application that calculates an employee's
bonus, tax deduction, and net salary based on their base salary and
performance rating.

## 📋 Project Description
This project demonstrates modular programming by separating the payroll
logic into independent functions:

- **`calculate_bonus(base_salary, performance_rating)`** 🎁
  Calculates the bonus based on performance rating:
  - Rating **5** → 20% bonus (Excellent performance) 🌟
  - Rating **3 or 4** → 10% bonus (Good performance) 👍
  - Rating **below 3** → 0% bonus (Needs improvement) 📉

- **`calculate_tax(gross_salary)`** 🧮
  Calculates the tax deduction based on gross salary
  (`base_salary + bonus`):
  - Gross salary **> 7000** → 15% tax
  - Gross salary **between 3000 and 7000** (inclusive) → 10% tax
  - Gross salary **below 3000** → 0% tax (exempt) ✅

- **`main_hr_app()`** ⚙️
  The controller function. Collects employee data (name, department,
  base salary, performance rating), validates the rating and salary,
  calls `calculate_bonus` and `calculate_tax` in sequence, and prints
  a formatted payroll statement.

## 🛠️ Installation Instructions
1. Make sure you have **Python 3.7+** installed:
```bash
   python3 --version
```
2. Clone or download this repository.
3. Navigate to the project folder:
```bash
   cd hr-payroll-app
```
4. No external libraries are required — the project only uses the
   Python standard library.

## ▶️ How to Run
```bash
python3 hr_payroll_app.py
```

You will be prompted to enter:
- 👤 Employee Name
- 🏢 Department Name
- 💰 Base Salary
- ⭐ Performance Rating (1–5)

## 🧾 Example Run
========================================
--- Corporate Payroll System ---
========================================
Enter Employee Name: rawan
Enter Department Name: IT 
Enter Base Salary: 30000
Enter Performance Rating (1-5): 4
========================================
 Payroll Statement For: Rawan
========================================
Base Salary      :  30,000.00 EGP
Earned Bonus     :  3,000.00 EGP
Gross Salary     :  33,000.00 EGP
Tax Deductions   :  4,950.00 EGP
----------------------------------------
NET PAYABLE CASH :  28050.00 EGP
========================================
