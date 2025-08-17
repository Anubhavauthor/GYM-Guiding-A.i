import json
import os
from datetime import datetime

# Step 1: Har din ka plan
weekly_plan = {
    "Monday": "Chest",
    "Tuesday": "Back",
    "Wednesday": "Legs",
    "Thursday": "Shoulders",
    "Friday": "Arms",
    "Saturday": "Full Body",
    "Sunday": "Rest"
}

# Step 2: Aaj ka din kya hai
today = datetime.now().strftime("%A")

if today == "Sunday":
    print("Aaj rest day hai. Recovery bhi zaroori hoti hai 💆‍♂️")
else:
    body_part = weekly_plan[today]

    # ✅ Step 3: Safe path banao JSON file ka
    base_dir = os.path.dirname(__file__)  # yeh current file ka folder path dega
    json_path = os.path.join(base_dir, 'data', 'exercise_data.json')  # dynamic path

    # Step 4: File read karo
    with open(json_path, 'r') as file:
        exercise_data = json.load(file)

    # Step 5: Exercise print karo
    if body_part in exercise_data:
        exercises = exercise_data[body_part]
        print(f"Aaj {body_part} ka workout hai 🏋️‍♂️")
        print("Aap ye exercises karein:")
        for ex in exercises:
            print(f"- {ex}")
    else:
        print(f"'{body_part}' ke liye exercise list nahi mili.")




import csv

# User se input lo workout ke baad
log_workout = input("Kya aap apna workout log karna chahenge? (yes/no): ").strip().lower()

if log_workout == "yes":
    log_date = datetime.now().strftime("%Y-%m-%d")  # aaj ki date
    log_body_part = input("Body part (e.g., Chest): ").strip()
    log_exercise = input("Exercise name (e.g., Push-ups): ").strip()
    log_sets = input("Number of sets: ").strip()
    log_reps = input("Number of reps: ").strip()
    log_weight = input("Weight used (kg): ").strip()

    # File ka path
    progress_file = os.path.join(base_dir, 'data', 'progress_log.csv')

    # CSV me likhna
    with open(progress_file, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([log_date, log_body_part, log_exercise, log_sets, log_reps, log_weight])

    print("✅ Workout log save ho gaya!")
else:
    print("Workout log skip kiya gaya.")

