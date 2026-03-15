# Mobile Recharge Calculator

print("------ MOBILE RECHARGE ------")

name = input("Enter customer name: ")
mobile = input("Enter mobile number: ")

print("\nRecharge Plans")
print("1. ₹199 Plan")
print("2. ₹399 Plan")
print("3. ₹599 Plan")

choice = int(input("Select your plan (1/2/3): "))

if choice == 1:
    amount = 199
    validity = 28
elif choice == 2:
    amount = 399
    validity = 56
elif choice == 3:
    amount = 599
    validity = 84
else:
    print("Invalid plan")
    amount = 0
    validity = 0

gst = amount * 0.18
total = amount + gst

print("\n------ BILL DETAILS ------")
print("Customer Name :", name)
print("Mobile Number :", mobile)
print("Plan Amount   :", amount)
print("GST (18%)     :", gst)
print("Total Amount  :", total)
print("Validity      :", validity, "Days")
