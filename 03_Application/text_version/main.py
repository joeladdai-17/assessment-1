# Student Revision Planner - Text Version 
# Creating the Main Menu

# display main menu
def display_mainMenu():
        print("---------- STUDENT REVISION PLANNER ----------")
        print("1. Dashboard")
        print("2. Manage Subjects and Topics")
        print("3. View Revision Timetable")
        print("4. Generate Revision Schedule")  
        print("5. View Priority Topics")
        print("6. Spaced Repetition")
        print("7. Progress Overview")
        print("8. Save and Load Data")
        print("9. Exit")

# Main menu loop
while True:
    display_mainMenu()
    choice = input("Enter an option [1-9]: ")

    # Handling users menu selection
    if choice == "1":
        print("Dashboard Selected")
        input("Press Enter to return to the Main Menu")

    elif choice == "2":
        print("Manage Subjects and Topics Selected")
        input("Press Enter to return to the Main Menu")

    elif choice == "3":
        print("View Revision Timetable Selected")
        input("Press Enter to return to the Main Menu")

    elif choice == "4":
        print("Generate Revision Schedule Selected")
        input("Press Enter to return to the Main Menu")

    elif choice == "5":
        print("View Priority Topics Selected")
        input("Press Enter to return to the Main Menu")

    elif choice == "6":
        print("Spaced Repetition Selected")
        input("Press Enter to return to the Main Menu")

    elif choice == "7":
        print("Progress Overview Selected")
        input("Press Enter to return to the Main Menu")

    elif choice == "8":
        print("Save and Load Data Selected")
        input("Press Enter to return to the Main Menu")

    elif choice == "9":
        print("Exit Selected")
        break

    else:
        print("Invalid choice. Enter an a number [1-9]")
        input("Press Enter to try again...")








