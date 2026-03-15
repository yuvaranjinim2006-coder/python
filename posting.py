name = input("Enter candidate name: ")
posting = input("Enter TNPSC posting place: ")
department = input("Enter department name: ")


name = name.strip()
posting = posting.strip()
department = department.strip()


name = name.title()
posting = posting.title()
department = department.upper()

print("\n--- TNPSC Posting Details ---")
print("Candidate Name :", name)
print("Posting Place  :", posting)
print("Department     :", department)
