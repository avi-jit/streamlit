import streamlit as st

# Define a list of days of the week
days_of_week = ["M", "T", "W", "H", "F"]

# Define a list of gym exercises
gym_exercises = ["LatPull", "Pushups", "Squats", "Lunges", "Press", "Curl", "Tricep"]

columns = st.columns([4]+[1]*len(days_of_week))
columns[0].text(".")
for exercise in gym_exercises:
    columns[0].text(exercise)
for i, col in enumerate(columns[1:]):
    col._width = 1
    col.text(days_of_week[i])
    # checkboxes
    for exercise in gym_exercises:
        col.checkbox("", key=f"{exercise}-{col}")