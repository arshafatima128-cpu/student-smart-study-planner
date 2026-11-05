print("================================")
print("   STUDENT SMART STUDY PLANNER")
print("================================")

name = input("Enter your name: ")

print("\nWelcome,", name)

subjects = []

while True:
    print("\n--- Study Planner Menu ---")
    print("1. Add Subject")
    print("2. View Subjects")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        subject = input("Enter subject name: ")
        subjects.append(subject)
        print("Subject added successfully!")

    elif choice == "2":
        print("\nYour Subjects:")
        if len(subjects) == 0:
            print("No subjects added yet.")
        else:
            for sub in subjects:
                print("-", sub)

    elif choice == "3":
        print("Thank you for using Study Planner!")
        break

    else:
        print("Invalid choice. Try again.")
      
