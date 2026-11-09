# Student Revision Planner - Text Version 

# 1. Imports
from core.subject import Subject
from core.topic import Topic

#2. Application data
subjects = []

#3. Subject and topic functions
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

#View Subject
def view_subject():
    if len(subjects) == 0:
        print("No subjects have been added yet")
    else:
        number = 1 #Numbering the list of subjects
        for item in subjects:
            print(f" {number}. {item.name} - Exam Date: {item.exam_date}")
            number += 1

#Edit Subject
def edit_subject():
    pass

#Delete Subject
def delete_subject():
    pass

#Add Topic
def add_topic():
    print("-----ADD TOPIC-----")
    view_subject()
    subject_choice = input("Enter one of the following subject numbers: ")
    subject_index = int(subject_choice)-1
    selected_subject = subjects[subject_index]
    topic_name = input("Enter topic name: ")
    topic_difficulty = int(input("Enter difficulty ([1-5], where 1 is easy and 5 is difficult)"))
    topic_confidence = int(input("Enter a confidence rating ([1-5], " \
    "where 1 is least confident and 5 is most confident)"))
    new_topic = Topic(topic_name, topic_difficulty, topic_confidence)
    selected_subject.add_topic(new_topic)
    print(f"Topic '{topic_name}' successfully added to {selected_subject.name}!")

#View Topic
def view_topic():
    if len(subjects) == 0:
        print("No subjects have been added yet")
    else:
        view_subject()

        subject_choice = input("Enter one of the following subject numbers: ")
        subject_index = int(subject_choice)-1

        if subject_index < 0 or subject_index >= len(subjects):
            print("Invalid subject number")
        else:
            selected_subject = subjects[subject_index]
            print(f"Topics for {selected_subject.name}:")

            if len(selected_subject.topics) == 0:
                print("No topics have been added yet")
            else:
                number = 1
                for topic in selected_subject.topics:
                    print(f"{number}. {topic.name}")
                    print(f"Difficulty: {topic.difficulty}/5")
                    print(f"Confidence: {topic.confidence}/5")
                    number += 1

        
#Updating confidence rating
def update_confidence():
    pass

#Edit topic
def edit_topic():
    pass

#Delete topic
def delete_topic():
    pass

#4. Revision functions
# Viewing Revision timetable
def view_timetable():
    pass


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
            add_subject()

        elif subMenu_choice == "2":
            view_subject()

        elif subMenu_choice == "3":
            add_topic()

        elif subMenu_choice == "4":
            view_topic()

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

def main():
    while True:
        display_mainMenu()
        mainMenu_choice = input("Enter an option [1-9]: ")

        # Handling users menu selection
        if mainMenu_choice == "1":
            print("Dashboard Selected")
            input("Press Enter to return to the Main Menu")

        elif mainMenu_choice == "2":
            #print("Manage Subjects and Topics Selected")
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

if __name__ == "__main__":
    main()