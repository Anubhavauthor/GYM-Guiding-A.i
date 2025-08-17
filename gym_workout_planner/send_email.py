import os
import json

# Step 1: Get current directory
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Step 2: Construct absolute path
json_path = os.path.join(BASE_DIR, 'workout_plan.json')

# Step 3: Load JSON
with open(json_path, 'r') as f:
    workout_plan = json.load(f)










import smtplib
import ssl
from email.message import EmailMessage
import datetime
import json
import os

# Email details
sender_email = "anubhavauthor.in@gmail.com"
receiver_email = "srivastavs791@gmail.com"
app_password = "pvok xwvr pkox hpot"

# Get today's day
today = datetime.date.today()
weekday = today.strftime('%A')
date_str = today.strftime('%Y-%m-%d')

# Load workout plan
try:
    with open("workout_plan.json", "r") as f:
        workout_data = json.load(f)
except Exception as e:
    print(f"❌ Failed to load workout plan: {e}")
    workout_data = {}

# Get today’s workout
today_workout = workout_data.get(weekday, [])

# Build the workout section
if today_workout:
    workout_details = "\n".join([
        f"👉 {ex['exercise']} - {ex['sets']} sets × {ex['reps']} reps\n🔗 [Watch]({ex['youtube']})"
        for ex in today_workout
    ])
else:
    workout_details = "🚫 Rest Day! Focus on recovery, stretching, or light cardio."

# Email body
body = f"""
Hey Anubhav 👋,

📅 Date: {date_str}
🗓️ Day: {weekday}

🏋️‍♂️ Today's Workout Plan:
{workout_details}

Keep grinding and stay consistent! 🔥🔥🔥
"""

# Create email
msg = EmailMessage()
msg['Subject'] = f"🏋️‍♂️ Workout Plan for {weekday} - {date_str}"
msg['From'] = sender_email
msg['To'] = receiver_email
msg.set_content(body)

# Attach chart only on Sunday
if weekday == 'Sunday':
    chart_path = 'progress_chart.png'
    if os.path.exists(chart_path):
        with open(chart_path, 'rb') as f:
            msg.add_attachment(f.read(), maintype='image', subtype='png', filename='progress_chart.png')

# Send email
try:
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, app_password)
        server.send_message(msg)
    print("✅ Email sent successfully!")
except Exception as e:
    print(f"❌ Failed to send email: {e}")
