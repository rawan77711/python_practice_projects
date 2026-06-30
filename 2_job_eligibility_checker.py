"""
job_eligibility_checker.py
A simple program to check job eligibility based on Python skills,
experience, and educational background.
"""

print("Do you master Python? Yes/No")
python=input().strip().lower()

print("How many years of experience or projects do you have? Enter a number")
experience=int(input())

print(
    "Do you have a university degree in computer science "
    "or have you completed an intensive training bootcamp? Yes/No"
)
degree=input().strip().lower()

if python=="yes" and (experience>=2 or degree=="yes"):
    print("Congratulations! You Have Been Accepted For The Next Stage of Interviews.")
else:
    print("Sorry, Your Current Qualifications Don\'t Match The Job Requirements.")
