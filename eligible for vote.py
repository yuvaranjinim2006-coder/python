# Voting Eligibility Program

print("------ VOTING ELIGIBILITY CHECKER ------")

name = input("Enter your name: ")
age = int(input("Enter your age: "))   # type conversion

print("\nHello", name)

if age >= 18:
    print("You are eligible for voting")
    
    voter_id = input("Do you have Voter ID (yes/no): ")
    
    if voter_id.lower() == "yes":
        print("You can vote in the election")
    else:
        print("Please apply for Voter ID")
        
else:
    years_left = 18 - age
    print("You are not eligible for voting")
    print("You can vote after", years_left, "years")

print("\nThank you for using Voting Eligibility Checker")
