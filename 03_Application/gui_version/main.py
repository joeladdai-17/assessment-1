# GUI Version
# Importing modules
import tkinter as tk
from tkinter import ttk
from datetime import datetime
from tkinter import messagebox
import sys
from pathlib import Path 
# importing the shared core classes
application_folder = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(application_folder))

from core.subject import Subject
from core.topic import Topic

subjects = []

# Windows and frames
root = tk.Tk()
root.title("Student Revision Planner")
root.geometry("900x600")

sidebar_frame = tk.Frame(root, bg="#1E293B", width=200)
sidebar_frame.grid(row=0, column=0, sticky="ns")

content_frame = tk.Frame(root, bg="#F1F5F9")
content_frame.grid(row=0, column=1, sticky="nsew")

root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

# GUI Functions
# clears the content area
def clear_content():
    for widget in content_frame.winfo_children():
        widget.destroy()

# displaying dashboard
def show_dashboard():
    clear_content()
    welcome_label = tk.Label(content_frame, 
                         text="Welcome to Student Revision Planner",
                         font=("Arial", 20, "bold"),
                         bg="#F1F5F9")

    welcome_label.grid(row=0, column=0, padx=30, pady=30)
    

# displaying subjects & topics window
def show_subjects_topics():
    clear_content()
    subject_topics_label = tk.Label(content_frame, 
            text="Manage Subjects and Topics",
            font=("Arial", 20, "bold"),
            bg="#F1F5F9")
    
    subject_topics_label.grid(row=0, column=0, padx=30, pady=30)

    # frames for buttons
    buttons_frame = tk.Frame(content_frame, bg="#F1F5F9")
    buttons_frame.grid(row=1, column=0, padx=30, pady=10)
    
    # creating add subject button 
    tk.Button(buttons_frame, text="Add Subject", command= show_add_subject_form, width=20).grid(row=0, column=0, padx=20, pady=10)

    # creating view subject button 
    tk.Button(buttons_frame, text="View Subjects", command= show_view_subjects, width=20).grid(row=1, column=0, padx=20, pady=10)

    # creating edit subject button 
    tk.Button(buttons_frame, text="Edit Subjects", command= show_edit_subject_form, width=20).grid(row=2, column=0, padx=20, pady=10)

    # creating delete subject button
    tk.Button(buttons_frame, text="Delete Subject", command=show_delete_subject_form, width=20).grid(row=3,column=0, padx=20, pady=10)
    
    # creating add topic button 
    tk.Button(buttons_frame, text="Add Topic", command=show_add_topic_form, width=20).grid(row=0, column=1, padx=20, pady=10)

    # creating view topic button
    tk.Button(buttons_frame, text="View Topics", command=show_view_topic_form, width=20).grid(row=1, column=1, padx=20, pady=10)

    #creating edit topic button 
    tk.Button(buttons_frame, text="Edit Topics", width=20).grid(row=2, column=1, padx=20, pady=10)

    #creating delete topic button 
    tk.Button(buttons_frame, text="Delete Topic", width=20).grid(row=3, column=1, padx=20, pady=10)


    
# add subject form
def show_add_subject_form():
    clear_content()
    add_subject_label = tk.Label(content_frame, 
        text="Add New Subject",
        font=("Arial", 20, "bold"),
        bg="#F1F5F9")
    add_subject_label.grid(row=0, column=0, padx=30, pady=30)

    # subject name
    subject_name_label = tk.Label(content_frame, 
        text="Subject Name:",
        font=("Arial", 14, "bold"),
                bg="#F1F5F9")
    subject_name_label.grid(row=1, column=0, padx=30, pady=30)

    # entry box
    subject_name_entry = tk.Entry(content_frame, width=25)
    subject_name_entry.grid(row=1, column=1, padx=10, pady=10)

    # exam date 
    exam_date_label = tk.Label(content_frame, 
            text="Exam Date (DD/MM/YYYY):",
            font=("Arial", 14, "bold"),
                    bg="#F1F5F9")
        
    exam_date_label.grid(row=2, column=0, padx=30, pady=30)

    exam_date_entry = tk.Entry(content_frame, width=25)
    exam_date_entry.grid(row=2, column=1, padx=10, pady=10)

# add subject
    def save_subject():
        name = subject_name_entry.get().strip()
        exam_date = exam_date_entry.get().strip()

        if name == "" or exam_date == "":
            messagebox.showerror("Error", "Please fill in all fields")
            return

        if name.isdigit():
            messagebox.showerror("Error", "Invalid subject name is purely numerical")
            return

        try:
            datetime.strptime(exam_date, "%d/%m/%Y")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid date")
            return

        newSubject = Subject(name, exam_date)
        subjects.append(newSubject)
        messagebox.showinfo("Success", f"{name} added successfully!")

    tk.Button(content_frame, 
        text="Save Subject", 
        command=save_subject,
        width=20).grid(row=3, column=0, columnspan=2, pady=20)

def show_view_subjects():
    clear_content()
    view_subject_label = tk.Label(content_frame, 
            text="View Subject",
            font=("Arial", 20, "bold"),
            bg="#F1F5F9")
    view_subject_label.grid(row=0, column=0, padx=30, pady=30)

    if len(subjects) == 0:
        no_subjects_label = tk.Label(content_frame, 
               text="No subjects",
               font=("Arial", 14, "bold"),
               bg="#F1F5F9")
        no_subjects_label.grid(row=1, column=0, padx=10, pady=10)

    row_number = 1

    for subject in subjects:
        subject_name_label = tk.Label(content_frame,
        text=subject.name,
        font=("Arial", 14, "bold"),
        bg="#F1F5F9")
        subject_name_label.grid(row=row_number, column=0, padx=30, pady=30)

        exam_date_label = tk.Label(content_frame,
                text=subject.exam_date,
                font=("Arial", 14, "bold"),
                bg="#F1F5F9")
        exam_date_label.grid(row=row_number, column=1, padx=30, pady=30)
        row_number += 1

def show_edit_subject_form():
    clear_content()
    edit_subject_label = tk.Label(content_frame, 
            text="Edit Subject",
            font=("Arial", 20, "bold"),
            bg="#F1F5F9")
    edit_subject_label.grid(row=0, column=0, padx=30, pady=30)

    if len(subjects) == 0:
            no_subjects_label = tk.Label(content_frame, 
                   text="No subjects",
                   font=("Arial", 14, "bold"),
                   bg="#F1F5F9")
            no_subjects_label.grid(row=1, column=0, padx=10, pady=10)
            return
    subject_names = []
    for subject in subjects:
        subject_names.append(subject.name)

    #combobox
    subject_dropdown = ttk.Combobox(content_frame, values=subject_names, state="readonly")
    subject_dropdown.grid(row=1, column=1, padx=10, pady=10)

    #Select subject label
    select_subject_label = tk.Label(content_frame, 
                text="Select Subject:",
                font=("Arial", 14, "bold"),
                bg="#F1F5F9")
    select_subject_label.grid(row=1, column=0, padx=30, pady=30)

    #New subject name label and entry
    new_subject_label = tk.Label(content_frame, 
                text="New Subject Name: ",
                font=("Arial", 14, "bold"),
                bg="#F1F5F9")
    new_subject_label.grid(row=2, column=0, padx=30, pady=30)

    new_subject_entry = tk.Entry(content_frame, width=25)
    new_subject_entry.grid(row=2, column=1, padx=10, pady=10)

    #New exam date label and entry
    new_exam_date_label = tk.Label(content_frame, 
                    text="New Exam date (DD/MM/YYYY): ",
                    font=("Arial", 14, "bold"),
                    bg="#F1F5F9")
    new_exam_date_label.grid(row=3, column=0, padx=30, pady=30)
    
    new_exam_date_entry = tk.Entry(content_frame, width=25)
    new_exam_date_entry.grid(row=3, column=1, padx=10, pady=10)

    def populate_fields(event):
        selected_index = subject_dropdown.current()
        selected_subject = subjects[selected_index]

        new_subject_entry.delete(0, tk.END)
        new_subject_entry.insert(0, selected_subject.name)

        new_exam_date_entry.delete(0, tk.END)
        new_exam_date_entry.insert(0, selected_subject.exam_date)

    subject_dropdown.bind("<<ComboboxSelected>>", populate_fields)

    def save_changes():
        selected_index = subject_dropdown.current()
        if selected_index == -1:
            messagebox.showerror("Error", "Please select a subject")
            return
        selected_subject = subjects[selected_index]
        # collecting entries
        new_name = new_subject_entry.get().strip()
        new_exam_date = new_exam_date_entry.get().strip()

        if new_name == "" or new_exam_date == "":
            messagebox.showerror("Error", "Please fill in all fields")
            return

        if new_name .isdigit():
            messagebox.showerror("Error", "Invalid subject name is purely numerical")
            return
        
        try:
            datetime.strptime(new_exam_date, "%d/%m/%Y")
        except ValueError:
            messagebox.showerror("Error", "Please enter a valid date")
            return
        
        selected_subject.name = new_name
        selected_subject.exam_date = new_exam_date

        subject_names[selected_index] = new_name
        subject_dropdown.configure(values=subject_names)
        subject_dropdown.current(selected_index)

        messagebox.showinfo("Success", f"{new_name} updated successfully!")

    #save button
    tk.Button(content_frame, text="Save Changes", command=save_changes, width=20).grid(row=4, column=0, columnspan=2, pady=20)

# delete subject
def show_delete_subject_form():
    clear_content()
    delete_subject_label = tk.Label(content_frame, 
                text="Delete Subject",
                font=("Arial", 20, "bold"),
                bg="#F1F5F9")
    delete_subject_label.grid(row=0, column=0, padx=30, pady=30)

    if len(subjects) == 0:
        tk.Label(content_frame, text="No subjects available to delete",
                bg="#F1F5F9").grid(row=1, column=0)
        return
    
    subject_names = []

    for subject in subjects:
        subject_names.append(subject.name) 

    subject_dropdown = ttk.Combobox(content_frame,
                                     values=subject_names,
                                     state="readonly")
    subject_dropdown.grid(row=1, column=1, padx=10, pady=10)

    tk.Label(content_frame, text="Select Subject:",
                    bg="#F1F5F9").grid(row=1, column=0)
    def delete_subject():
        selected_index = subject_dropdown.current()

        if selected_index == -1:
            messagebox.showerror("Error", "Please select a subject")
            return

        selected_subject = subjects[selected_index]

        #confirmation message
        confirm = messagebox.askyesno("Confirm Deletion",
                                       f"Are you sure you want to delete {selected_subject.name}?")

        if confirm:
            subjects.pop(selected_index)
            show_delete_subject_form()
            messagebox.showinfo("Success", f"You have successfully deleted {selected_subject.name}")

# delete button
    tk.Button(content_frame, text="Delete Subject", command=delete_subject, width=20).grid(row=2, column=0, columnspan=2, pady=20)  

# Topic
def show_add_topic_form():
    # checking if theres no subjects available
    if len(subjects) == 0:
        messagebox.showerror("Error", "No subjects available")
        return
    clear_content()
    
    add_topic_label = tk.Label(content_frame, 
            text="Add Topic",
            font=("Arial", 20, "bold"),
            bg="#F1F5F9")
    add_topic_label.grid(row=0, column=0, padx=30, pady=30)

    subject_names = []
    for subject in subjects:
        subject_names.append(subject.name)

    select_subject_dropdown = ttk.Combobox(content_frame, values=subject_names, state="readonly")
    select_subject_dropdown.grid(row=1, column=1, padx=10, pady=10)

    select_subject_label = tk.Label(content_frame, 
                text="Select Subject: ",
                font=("Arial", 15, "bold"),
                bg="#F1F5F9")
    select_subject_label.grid(row=1, column=0, padx=30, pady=30)

    # topic name label and entry field
    topic_name_label = tk.Label(content_frame, 
                text="Topic Name: ",
                font=("Arial", 15, "bold"),
                bg="#F1F5F9")
    topic_name_label.grid(row=2, column=0, padx=30, pady=30)

    topic_name_entry = tk.Entry(content_frame, width=25)
    topic_name_entry.grid(row=2, column=1, padx=10, pady=10)

    # difficulty label and dropdown
    difficulty_label = tk.Label(content_frame, 
                       text="Difficulty (1-5): ",
                       font=("Arial", 15, "bold"),
                       bg="#F1F5F9")
    difficulty_label.grid(row=3, column=0, padx=30, pady=30)
    
    difficulty_dropdown = ttk.Combobox(content_frame, values=[1, 2, 3, 4, 5], state="readonly")
    difficulty_dropdown.grid(row=3, column=1, padx=10, pady=10)
    
    # confidence label and dropdown 
    confidence_label = tk.Label(content_frame, 
                    text="Confidence (1-5): ",
                    font=("Arial", 15, "bold"),
                    bg="#F1F5F9")
    confidence_label.grid(row=4, column=0, padx=30, pady=30)

    confidence_dropdown = ttk.Combobox(content_frame, values=[1, 2, 3, 4, 5], state="readonly")
    confidence_dropdown.grid(row=4, column=1, padx=10, pady=10)

    

    #add topic functionality
    def add_topic():
        select_subject = select_subject_dropdown.get()
        topic_name = topic_name_entry.get().strip()
        difficulty = difficulty_dropdown.get()
        confidence = confidence_dropdown.get()

        # making sure the user doesnt leave blank options
        if select_subject == "":
            messagebox.showerror("Error", "Please select a subject")
            return

        if topic_name == "":
            messagebox.showerror("Error", "Please enter the topic")
            return

        if difficulty == "":
            messagebox.showerror("Error", "Please select a difficulty rating [1-5]")
            return

        if confidence == "":
            messagebox.showerror("Error", "Please select a confidence rating [1-5]")
            return

        # converting difficulty and confidence selected ratings into integers
        difficulty = int(difficulty)
        confidence = int(confidence)

        for subject in subjects:
            if subject.name == select_subject:
                new_topic = Topic(topic_name, difficulty, confidence)
                subject.add_topic(new_topic)
                messagebox.showinfo("Success", f"{topic_name} added successfully!")
                return
            
    # add topic button
    tk.Button(content_frame, text="Add Topic", command=add_topic, width=20).grid(row=5, column=1, padx=10, pady=10)

# view topics
def show_view_topic_form():
    # checking if theres no subjects available
    if len(subjects) == 0:
        messagebox.showerror("Error", "No subjects available")
        return
    clear_content()
    view_topic_label = tk.Label(content_frame, 
                text="View Topics",
                font=("Arial", 20, "bold"),
                bg="#F1F5F9")
    view_topic_label.grid(row=0, column=0, padx=30, pady=30)

    subject_names = []
    for subject in subjects:
        subject_names.append(subject.name)
    
    select_subject_label = tk.Label(content_frame, 
                    text="Select Subject: ",
                    font=("Arial", 15, "bold"),
                    bg="#F1F5F9")
    select_subject_label.grid(row=1, column=0, padx=30, pady=30)

    select_subject_dropdown = ttk.Combobox(content_frame, values=subject_names, state="readonly")
    select_subject_dropdown.grid(row=1, column=1, padx=10, pady=10)

    #view topics functionality
    def view_topics():
        select_subject = select_subject_dropdown.get()
        if select_subject == "":
            messagebox.showerror("Error","Please select a subject")
            return

        for subject in subjects:
            if subject.name == select_subject:
                if len(subject.topics) == 0:
                    messagebox.showinfo("Information", "No topics available for this subject")
                    return

                #headings for topic name, difficulty and confidence
                topic_name_heading = tk.Label(content_frame,
                                    text="Topic Name",
                                    font=("Arial", 14, "bold"),
                                    bg="#F1F5F9")
                topic_name_heading.grid(row=3, column=0, padx=30, pady=30)

                difficulty_heading = tk.Label(content_frame,
                                    text="Difficulty",
                                    font=("Arial", 14, "bold"),
                                    bg="#F1F5F9")
                difficulty_heading.grid(row=3, column=1, padx=30, pady=30)

                confidence_heading = tk.Label(content_frame,
                                                    text="Confidence",
                                                    font=("Arial", 14, "bold"),
                                                    bg="#F1F5F9")
                confidence_heading.grid(row=3, column=2, padx=30, pady=30)

                row_number = 4
                for topic in subject.topics:
                    topic_name_label = tk.Label(content_frame,
                            text=topic.name,
                            font=("Arial", 14, "bold"),
                            bg="#F1F5F9")
                    topic_name_label.grid(row=row_number, column=0, padx=30, pady=30)
                    
                    difficulty_label = tk.Label(content_frame,
                            text=topic.difficulty,
                            font=("Arial", 14, "bold"),
                            bg="#F1F5F9")
                    difficulty_label.grid(row=row_number, column=1, padx=30, pady=30)

                    confidence_label = tk.Label(content_frame,
                            text=topic.confidence,
                            font=("Arial", 14, "bold"),
                            bg="#F1F5F9")
                    confidence_label.grid(row=row_number, column=2, padx=30, pady=30)

                    row_number += 1
                

    #view button 
    tk.Button(content_frame, text="View Topics",command=view_topics, width=20).grid(row=2, column=1, padx=10, pady=10)
    


#Buttons
tk.Button(sidebar_frame, text="Dashboard", command= show_dashboard, width=20).grid(row=0, column=0, padx=10, pady=10)
tk.Button(sidebar_frame, text="Subjects & Topics", command = show_subjects_topics, width=20).grid(row=1, column=0, padx=10, pady=10)
tk.Button(sidebar_frame, text="Revision Timetable", width=20).grid(row=2, column=0, padx=10, pady=10)
tk.Button(sidebar_frame, text="Priority Topics", width=20).grid(row=3, column=0, padx=10, pady=10)
tk.Button(sidebar_frame, text="Save / Load", width=20).grid(row=4, column=0, padx=10, pady=10)
tk.Button(sidebar_frame, text="Exit", command = root.destroy, width=20).grid(row=5, column=0, padx=10, pady=10)

# Running application
show_dashboard()
root.mainloop()
