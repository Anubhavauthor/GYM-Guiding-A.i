import os
import json

# Step 1: Get current directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Step 2: Construct absolute path
json_path = os.path.join(BASE_DIR, 'workout_plan.json')

# Step 3: Load JSON
with open(json_path, 'r') as f:
    workout_plan = json.load(f)





import csv
from datetime import datetime

def log_progress():
    date = datetime.now().strftime('%Y-%m-%d')
    weight = input("🏋️ Enter your weight (kg): ")
    note = input("📝 Add any notes (optional): ")

    with open("progress_log.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([date, weight, note])
        print("✅ Progress logged successfully!")

if __name__ == "__main__":
    log_progress()
