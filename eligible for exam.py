name = input("Enter student name: ")
register_no = input("Enter register number: ")
attendance = int(input("Enter attendance percentage: "))

if attendance >= 75:
    print("Student Name:", name)
    print("Register Number:", register_no)
    print("You are eligible for exam")
else:
    print("Student Name:", name)
    print("Register Number:", register_no)
    print("You are not eligible for exam due to low attendance")
