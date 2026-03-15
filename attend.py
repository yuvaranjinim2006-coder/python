n = int(input("Enter number of students: "))

for i in range(n):
    name = input("Enter student name: ")
    total_classes = int(input("Enter total classes: "))
    attended_classes = int(input("Enter attended classes: "))

    percentage = (attended_classes / total_classes) * 100

    if percentage >= 75:
        print(name, "is eligible for exam")
    else:
        print(name, "is not eligible for exam")
