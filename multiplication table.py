# Multiplication Table Program (Big Version)

print("------ MULTIPLICATION TABLE GENERATOR ------")

name = input("Enter your name: ")
num = int(input("Enter a number to generate table: "))
limit = int(input("Enter table limit: "))

print("\nHello", name)
print("Multiplication Table for", num)
print("-" * 30)

for i in range(1, limit + 1):
    result = num * i
    print(num, "x", i, "=", result)

print("-" * 30)

# Extra check
if num % 2 == 0:
    print(num, "is an Even number")
else:
    print(num, "is an Odd number")

print("Program Finished")
