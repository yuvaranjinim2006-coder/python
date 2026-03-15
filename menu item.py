# Juice Shop Menu Items

print("------ JUICE SHOP MENU ------")

print("1. Apple Juice      - ₹50")
print("2. Mango Juice      - ₹60")
print("3. Orange Juice     - ₹40")
print("4. Pineapple Juice  - ₹70")
print("5. Watermelon Juice - ₹45")

choice = int(input("Select your juice (1-5): "))
qty = int(input("Enter quantity: "))

if choice == 1:
    price = 50
    juice = "Apple Juice"

elif choice == 2:
    price = 60
    juice = "Mango Juice"

elif choice == 3:
    price = 40
    juice = "Orange Juice"

elif choice == 4:
    price = 70
    juice = "Pineapple Juice"

elif choice == 5:
    price = 45
    juice = "Watermelon Juice"

else:
    print("Invalid choice")
    price = 0
    juice = "None"

total = price * qty

print("\n------ BILL ------")
print("Juice Name :", juice)
print("Price      :", price)
print("Quantity   :", qty)
print("Total Bill :", total)
