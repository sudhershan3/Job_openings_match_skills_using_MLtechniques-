import tkinter as tk
from tkinter import ttk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
import random

# Placeholder function to read data from CSV (replace with actual implementation)
def read_csv_data(filename):
    # Read and process data from CSV
    description_to_skills = {}  # Dictionary to store description to skills mapping
    # Implement your logic to read data from the CSV and populate description_to_skills
    return description_to_skills

# GUI
def on_match_button():
    input_skills = input_text.get("1.0", "end-1c").split(",")
    input_skills = [skill.strip().lower().replace(" ", "") for skill in input_skills]

    # Preprocess skills: lowercase and remove spaces
    preprocessed_skills = [" ".join(skill.split()) for skill in input_skills]

    # Combine description and preprocessed skills for vectorization
    descriptions = list(description_to_skills.keys())
    descriptions.extend(preprocessed_skills)

    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(descriptions)

    # Simulated job labels
    job_labels = [random.choice([0, 1]) for _ in range(X.shape[0])]

    # Train the Random Forest classifier
    model = RandomForestClassifier()
    model.fit(X, job_labels)

    input_vector = vectorizer.transform([" ".join(preprocessed_skills)])
    result = model.predict(input_vector)[0]

    suggested_jobs = []

    for description, skills in description_to_skills.items():
        job_vector = vectorizer.transform([description])
        job_label = model.predict(job_vector)[0]
        if job_label == result:
            suggested_jobs.append(description)

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
