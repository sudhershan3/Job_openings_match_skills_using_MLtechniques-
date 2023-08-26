import pandas as pd

def read_csv_data(csv_filename):
    df = pd.read_csv(csv_filename)
    description_to_skills = {}
    for index, row in df.iterrows():
        description = row["jobtitle"]
        skills = row["skills"].split(",") if pd.notnull(row["skills"]) else []
        description_to_skills[description] = [skill.strip().lower().replace(" ", "") for skill in skills]
    return description_to_skills
