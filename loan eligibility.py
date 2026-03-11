age = int(input("Age: "))
salary = int(input("Salary: "))

if age >= 21:
    if salary >= 20000:
        print("Loan Approved")
    else:
        print("Salary not enough")
else:
    print("Age not eligible")
