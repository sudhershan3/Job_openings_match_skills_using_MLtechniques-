import tkinter as tk
from tkinter import ttk
from data_processing import read_csv_data

# GUI
def on_match_button():
    input_skills = input_text.get("1.0", "end-1c").split(",")
    input_skills = [skill.strip().lower().replace(" ", "") for skill in input_skills]

    matching_jobs = {}

    for description, skills in description_to_skills.items():
        matching_count = sum(1 for skill in input_skills if skill in skills)
        if matching_count >= len(input_skills) // 2:  # Majority matching condition
            matching_jobs[description] = matching_count

    suggested_jobs = set()

    for job_description in matching_jobs:
        if matching_jobs[job_description] >= len(input_skills) // 2:
            suggested_jobs.add(job_description)

    job_list.delete(0, "end")
    for job_description in suggested_jobs:
        job_list.insert("end", job_description)

root = tk.Tk()
root.title("Job Matching")

# Textbox for inputting skills
input_label = ttk.Label(root, text="Enter your skills (comma-separated):")
input_text = tk.Text(root, height=1, width=40)
input_label.pack()
input_text.pack()

# Button to trigger job suggestions
match_button = ttk.Button(root, text="Find Suitable Jobs", command=on_match_button)
match_button.pack()

# Listbox to display suggested job descriptions
job_list = tk.Listbox(root, height=10, width=60)  # Increased width for better display
job_list.pack()

# Read data from CSV
csv_filename = "dice_com-job_us_sample.csv"  # Replace with your CSV filename
description_to_skills = read_csv_data(csv_filename)

root.mainloop()
