# GUI Version
# Importing modules
import tkinter as tk
from datetime import datetime
from tkinter import messagebox
import sys
from pathlib import Path 
# importing the shared core classes
application_folder = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(application_folder))

from core.subject import Subject

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
    tk.Button(buttons_frame, text="View Subjects", command= show_view_subjects, width=20).grid(row=0, column=1, padx=20, pady=10)

    # creating add topic button 
    tk.Button(buttons_frame, text="Add Topic", width=20).grid(row=1, column=0, padx=20, pady=10)

    # creating view topic button
    tk.Button(buttons_frame, text="View Topics", width=20).grid(row=1, column=1, padx=20, pady=10)

    
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


    def save_subject():
        name = subject_name_entry.get().strip()
        exam_date = exam_date_entry.get().strip()

        if name == "" or exam_date == "":
            messagebox.showerror("Error", "Please fill in all fields")
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
