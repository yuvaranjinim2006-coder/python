

name = input("Enter your name: ")
age = int(input("Enter your age: "))          
height = float(input("Enter your height: "))


age_str = str(age)z
height_int = int(height)


age_float = float(age)

is_adult = bool(age >= 18)

print("\n--- Converted Values ---")
print("Name:", name)
print("Age (string):", age_str)
print("Age (float):", age_float)
print("Height (int):", height_int)
print("Adult Status:", is_adult)


next_year_age = age + 1
print("Next year age:", next_year_age)

numbers = "1 2 3 4 5"
num_list = list(numbers)

print("List conversion:", num_list)
