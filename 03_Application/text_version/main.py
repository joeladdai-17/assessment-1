# Student Revision Planner - Text Version 
# importing Subject class from subject file
from core.subject import Subject
subjects = []
#View Subject
def view_subject():
    for item in subjects:
        print(f" {item.name} - Exam Date: {item.exam_date}")
        
# Add Subject
def add_subject():
    # name and exam date
    subjectName = input("Enter subject name: ")
    subject_examDate = input("Enter exam date: (DD/MM/YYYY)")
    newSubject = Subject(subjectName, subject_examDate)
    subjects.append(newSubject)
    print(f"{subjectName} has been added successfully")
    # checking how many subjects are stored temporarily
    print(len(subjects))
# Creating the Main Menu

# Display 2. Manage Subjects and Topics Menu
def manage_subMenu():
    # Sub-menu loop (Manage Subjects and Topics)
    while True:
        print("---------- MANAGE SUBJECTS AND TOPICS ----------")
        print("1. Add Subjects")
        print("2. View Subjects")
        print("3. Add Topic")
        print("4. View Topic")
        print("5. Return to Main Menu")

        subMenu_choice = input("Enter an option [1-5]: ")

        if subMenu_choice == "1":
            #print("Add Subjects Selected")
            #input("Press Enter to return to the Manage Subjects and Topics Menu")
            add_subject()

        elif subMenu_choice == "2":
            #print("View Subjects Selected")
            #input("Press Enter to return to the Manage Subjects and Topics Menu")
            view_subject()

        elif subMenu_choice == "3":
            print("Add Topic Selected")
            input("Press Enter to return to the Manage Subjects and Topics Menu")

        elif subMenu_choice == "4":
            print("View Topic Selected")
            input("Press Enter to return to the Manage Subjects and Topics Menu")

        elif subMenu_choice == "5":
            print("Returning to Main Menu")
            break
        
        else:
            print("Invalid choice. Enter an a number [1-5]")
            input("Press Enter to try again...")


# Display Main Menu
def display_mainMenu():
        print("----------STUDENT REVISION PLANNER ----------")
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
    mainMenu_choice = input("Enter an option [1-9]: ")

    # Handling users menu selection
    if mainMenu_choice == "1":
        print("Dashboard Selected")
        input("Press Enter to return to the Main Menu")

    elif mainMenu_choice == "2":
        #print("Manage Subjects and Topics Selected")
        #input("Press Enter to continue")
        manage_subMenu()
        
    elif mainMenu_choice == "3":
        print("View Revision Timetable Selected")
        input("Press Enter to return to the Main Menu")

    elif mainMenu_choice == "4":
        print("Generate Revision Schedule Selected")
        input("Press Enter to return to the Main Menu")

    elif mainMenu_choice == "5":
        print("View Priority Topics Selected")
        input("Press Enter to return to the Main Menu")

    elif mainMenu_choice == "6":
        print("Spaced Repetition Selected")
        input("Press Enter to return to the Main Menu")

    elif mainMenu_choice == "7":
        print("Progress Overview Selected")
        input("Press Enter to return to the Main Menu")

    elif mainMenu_choice == "8":
        print("Save and Load Data Selected")
        input("Press Enter to return to the Main Menu")

    elif mainMenu_choice == "9":
        print("Exit Selected")
        break

    else:
        print("Invalid choice. Enter an a number [1-9]")
        input("Press Enter to try again...")