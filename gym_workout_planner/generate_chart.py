import os
import json

# Step 1: Get current directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Step 2: Construct absolute path
json_path = os.path.join(BASE_DIR, 'workout_plan.json')

# Step 3: Load JSON
with open(json_path, 'r') as f:
    workout_plan = json.load(f)



import pandas as pd
import matplotlib.pyplot as plt

try:
    # Try with correct relative path
    df = pd.read_csv('gym_workout_planner/data/progress_log.csv')  # <- Full path
    df['date'] = pd.to_datetime(df['date'])
    df = df.sort_values(by='date')

    plt.figure(figsize=(10, 5))
    plt.plot(df['date'], df['weight_kg'], marker='o', linestyle='-', color='blue')
    plt.title('📉 Bodyweight Progress Over Time')
    plt.xlabel('Date')
    plt.ylabel('Weight (kg)')
    plt.grid(True)
    plt.tight_layout()
    plt.savefig('progress_chart.png')
    plt.show()

    print("✅ Chart saved as progress_chart.png")

except Exception as e:
    print(f"❌ Error: {e}")
