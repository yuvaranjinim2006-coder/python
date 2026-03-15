# Advanced Age Calculator

from datetime import date

print("------ AGE CALCULATOR ------")

name = input("Enter your name: ")

birth_day = int(input("Enter birth day: "))
birth_month = int(input("Enter birth month: "))
birth_year = int(input("Enter birth year: "))

today = date.today()

current_day = today.day
current_month = today.month
current_year = today.year

age_year = current_year - birth_year
age_month = current_month - birth_month
age_day = current_day - birth_day

if age_day < 0:
    age_month -= 1
    age_day += 30

if age_month < 0:
    age_year -= 1
    age_month += 12

print("\nHello", name)
print("Your Age is:")
print(age_year, "Years", age_month, "Months", age_day, "Days")

# Eligibility check
if age_year >= 18:
    print("You are eligible for voting")
else:
    print("You are not eligible for voting")
