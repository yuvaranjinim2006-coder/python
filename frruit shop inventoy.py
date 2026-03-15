

inventory = {
    "apple": 50,
    "banana": 40,
    "orange": 30
}

while True:
    print("\n--- Fruit Shop Inventory ---")
    print("1. View Inventory")
    print("2. Add Fruit")
    print("3. Sell Fruit")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\nAvailable Fruits:")
        for fruit, qty in inventory.items():
            print(fruit, ":", qty)

    elif choice == "2":
        fruit = input("Enter fruit name: ").lower()
        qty = int(input("Enter quantity to add: "))

        if fruit in inventory:
            inventory[fruit] += qty
        else:
            inventory[fruit] = qty

        print("Fruit added successfully!")

    elif choice == "3":
        fruit = input("Enter fruit name to sell: ").lower()
        qty = int(input("Enter quantity to sell: "))

        if fruit in inventory:
            if inventory[fruit] >= qty:
                inventory[fruit] -= qty
                print("Sale successful!")
            else:
                print("Not enough stock!")
        else:
            print("Fruit not found!")

    elif choice == "4":
        print("Thank you! Visit again.")
        break

    else:
        print("Invalid choice!")
