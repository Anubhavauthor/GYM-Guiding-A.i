from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.uix.boxlayout import BoxLayout

import json
import csv
import datetime
from datetime import date
import os

# Set background color
Window.clearcolor = (0, 0, 0, 1)

# ---------- Workout Screen ----------
class WorkoutScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

        title = Label(text="Today's Workout Plan", font_size=24, color=(1, 1, 1, 1))
        layout.add_widget(title)

        workout_data = self.get_today_workout()
        if workout_data:
            for exercise in workout_data:
                line = f"{exercise['exercise']} - {exercise['sets']} sets x {exercise['reps']} reps"
                layout.add_widget(Label(text=line, color=(1, 1, 1, 1)))
        else:
            layout.add_widget(Label(text="No workout today! Rest and recover.", color=(1, 1, 1, 1)))

        # Button to switch to progress screen
        progress_button = Button(text="Log Today's Weight", size_hint=(1, 0.2))
        progress_button.bind(on_press=lambda x: setattr(self.manager, 'current', 'progress'))
        layout.add_widget(progress_button)


        
        self.add_widget(layout)

    def get_today_workout(self):
        try:
            file_path = os.path.join(os.path.dirname(__file__), 'workout_plan.json')
            with open(file_path) as f:

                plan = json.load(f)
                today = datetime.datetime.now().strftime("%A")
                return plan.get(today, [])
        except Exception as e:
            print(f"Error loading workout plan: {e}")
            return []

# ---------- Log Progress Screen ----------
class ProgressScreen(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        layout = BoxLayout(orientation='vertical', spacing=20, padding=40)

        self.input = TextInput(hint_text="Enter today's weight (kg)", multiline=False, input_filter='float')
        submit_btn = Button(text='Log Progress', size_hint=(1, 0.3))
        submit_btn.bind(on_press=self.log_progress)

        layout.add_widget(self.input)
        layout.add_widget(submit_btn)

        self.add_widget(layout)

    def log_progress(self, instance):
        weight = self.input.text.strip()

        if not weight:
            self.show_popup("Error", "Please enter a weight.")
            return

        today = date.today().isoformat()
        file_path = os.path.join(os.path.dirname(__file__), 'data', 'progress_log.csv')

        try:
            file_exists = os.path.isfile(file_path)
            with open(file_path, 'a', newline='') as f:
                writer = csv.writer(f)
                if not file_exists:
                    writer.writerow(['Date', 'Weight'])
                writer.writerow([today, weight])

            self.show_popup("Success", f"Logged {weight} kg for {today}")
            self.input.text = ''
        except Exception as e:
            self.show_popup("Error", str(e))

    def show_popup(self, title, message):
        popup_layout = BoxLayout(orientation='vertical', padding=10)
        popup_layout.add_widget(Label(text=message))
        close_button = Button(text="OK", size_hint=(1, 0.25))
        popup_layout.add_widget(close_button)

        popup = Popup(title=title, content=popup_layout, size_hint=(0.7, 0.4))
        close_button.bind(on_press=popup.dismiss)
        popup.open()




# ---------- App Root ----------
class GymPlannerApp(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(WorkoutScreen(name='workout'))
        sm.add_widget(ProgressScreen(name='progress'))
        return sm

if __name__ == '__main__':
    GymPlannerApp().run()
