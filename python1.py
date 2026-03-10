import random

name = input("Enter your name: ")


name = name.replace(" ", "")


name = name.lower()

rev = name[::-1]


if len(name) < 4:
    print("Name must be at least 4 characters")

else:
    
    part = name[:4]

    
    num = random.randint(10,99)

    username = part + "_" + str(num)

    print("Generated Username:", username)


    print("Length of username:", len(username))
    print("Starts with letter a?:", username.startswith("a"))
    print("Is number?:", username.isdigit())
