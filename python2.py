import random

name = input("Enter your full name: ")
year = input("Enter your birth year: ")

name = name.lower().strip()
parts = name.split()

if len(parts) < 2:
    print("Enter first name and last name")

elif not year.isdigit():
    print("Birth year must be numbers")

else:
    first = parts[0]
    last = parts[1]

    f3 = first[:3]
    l3 = last[:3]

    num = random.randint(10, 99)

    domains = ["@gmail.com", "@yahoo.com", "@outlook.com"]

    print("Generated Emails:")

    for d in domains:
        email1 = first + last + d
        email2 = f3 + l3 + year + d
        email3 = first + str(num) + d

        print(email1)
        print(email2)
        print(email3)
        print("------")

