# ============================================================
# COACHBOT AI – ADVANCED DISTINCTION VERSION
# Single File – Production Level Streamlit App
# ============================================================

import streamlit as st
import google.generativeai as genai
import pandas as pd
from datetime import datetime
import os

# ------------------------------------------------------------
# PAGE CONFIG
# ------------------------------------------------------------
st.set_page_config(
    page_title="CoachBot AI – Advanced",
    page_icon="🏆",
    layout="wide"
)

# ------------------------------------------------------------
# API CONFIG
# ------------------------------------------------------------
# ------------------------------------------------------------
# API CONFIG
# ------------------------------------------------------------


API_KEY = "AIzaSyDiDcZ3_h4Q2Z_CQDjbFvL0c2LZwo94Ts0"

genai.configure(api_key=API_KEY)

# ------------------------------------------------------------
# SIDEBAR NAVIGATION
# ------------------------------------------------------------
st.sidebar.title("🏆 CoachBot Navigation")

page = st.sidebar.radio(
    "Go To:",
    [
        "Generate Coaching Plan",
        "Quick Workout Generator",
        "Nutrition Planner",
        "Injury Recovery Mode",
        "Tactical Intelligence",
        "Progress Tracker",
        "Macro Calculator",
        "Session History"
    ]
)

# ------------------------------------------------------------
# SESSION STATE STORAGE
# ------------------------------------------------------------
if "history" not in st.session_state:
    st.session_state.history = []

# ------------------------------------------------------------
# ATHLETE PROFILE (COMMON INPUT)
# ------------------------------------------------------------
st.sidebar.markdown("---")
st.sidebar.header("📋 Athlete Profile")

sport = st.sidebar.selectbox(
    "Sport",
    ["Football", "Cricket", "Basketball", "Athletics", "Tennis", "Badminton", "Other"]
)

position = st.sidebar.text_input("Position")

age = st.sidebar.slider("Age", 10, 25, 16)

injury = st.sidebar.text_input("Injury (Type None if no injury)")

goal = st.sidebar.selectbox(
    "Primary Goal",
    ["Build Stamina", "Increase Strength", "Improve Speed",
     "Post-Injury Recovery", "Skill Improvement",
     "Tournament Preparation", "Weight Management"]
)

diet_type = st.sidebar.selectbox(
    "Diet Preference",
    ["Vegetarian", "Non-Vegetarian", "Vegan", "No Preference"]
)

intensity = st.sidebar.selectbox(
    "Training Intensity",
    ["Low", "Moderate", "High"]
)

coach_style = st.sidebar.selectbox(
    "Coach Personality",
    ["Strict Professional Coach",
     "Friendly Motivational Coach",
     "Sports Scientist Analytical Coach"]
)

temperature = st.sidebar.slider("Creativity Level", 0.1, 1.0, 0.4)

# ------------------------------------------------------------
# GEMINI MODEL
# ------------------------------------------------------------
def call_gemini(prompt):
    model = genai.GenerativeModel("gemini-1.5-pro")

    response = model.generate_content(
        prompt,
        generation_config={
            "temperature": temperature,
            "top_p": 0.9,
            "top_k": 40
        }
    )

    return response.text


# ------------------------------------------------------------
# FEATURE 1 – FULL COACHING PLAN
# ------------------------------------------------------------
if page == "Generate Coaching Plan":

    st.title("🏆 Complete AI Coaching Plan")

    if st.button("Generate Plan"):

        prompt = f"""
You are a {coach_style}.

Athlete:
Sport: {sport}
Position: {position}
Age: {age}
Injury: {injury}
Goal: {goal}
Intensity: {intensity}
Diet: {diet_type}

Generate:
1. Weekly structured plan (Mon–Sun)
2. Warm-up & Cool-down
3. Injury-safe adjustments
4. Tactical advice for position
5. 1-day meal plan
6. Hydration plan
7. Mental focus routine
8. Recovery strategy
9. Performance metrics to track
10. Motivation message

Keep it safe for youth athletes.
"""

        with st.spinner("Generating advanced plan..."):
            output = call_gemini(prompt)

        st.write(output)

        st.session_state.history.append({
            "time": datetime.now(),
            "feature": "Full Plan",
            "output": output
        })


# ------------------------------------------------------------
# FEATURE 2 – QUICK WORKOUT GENERATOR
# ------------------------------------------------------------
elif page == "Quick Workout Generator":

    st.title("⚡ 20-Minute Smart Workout")

    if st.button("Generate Quick Session"):

        prompt = f"""
Create a 20-minute efficient workout for a {position} in {sport}.
Age: {age}
Injury: {injury}
Goal: {goal}
Keep it intense but safe.
"""

        output = call_gemini(prompt)
        st.write(output)


# ------------------------------------------------------------
# FEATURE 3 – NUTRITION PLANNER
# ------------------------------------------------------------
elif page == "Nutrition Planner":

    st.title("🥗 AI Nutrition Guide")

    if st.button("Generate Nutrition Plan"):

        prompt = f"""
Create a weekly nutrition plan for:
Sport: {sport}
Age: {age}
Goal: {goal}
Diet: {diet_type}
Include macros, hydration, and recovery foods.
"""

        output = call_gemini(prompt)
        st.write(output)


# ------------------------------------------------------------
# FEATURE 4 – INJURY RECOVERY MODE
# ------------------------------------------------------------
elif page == "Injury Recovery Mode":

    st.title("🩹 Recovery Training")

    if st.button("Generate Recovery Plan"):

        prompt = f"""
Design a safe recovery program for:
Sport: {sport}
Position: {position}
Injury: {injury}
Age: {age}
Include mobility, low-impact cardio, and gradual return plan.
"""

        output = call_gemini(prompt)
        st.write(output)


# ------------------------------------------------------------
# FEATURE 5 – TACTICAL INTELLIGENCE
# ------------------------------------------------------------
elif page == "Tactical Intelligence":

    st.title("🧠 Tactical Game Intelligence")

    if st.button("Generate Tactical Advice"):

        prompt = f"""
Provide advanced tactical advice for a {position} in {sport}.
Include:
- Decision making
- Position awareness
- Match scenarios
- Mistake reduction
"""

        output = call_gemini(prompt)
        st.write(output)


# ------------------------------------------------------------
# FEATURE 6 – PROGRESS TRACKER
# ------------------------------------------------------------
elif page == "Progress Tracker":

    st.title("📊 Weekly Progress Tracker")

    stamina = st.slider("Stamina Level", 1, 10, 5)
    strength = st.slider("Strength Level", 1, 10, 5)
    speed = st.slider("Speed Level", 1, 10, 5)

    data = pd.DataFrame({
        "Metric": ["Stamina", "Strength", "Speed"],
        "Score": [stamina, strength, speed]
    })

    st.bar_chart(data.set_index("Metric"))


# ------------------------------------------------------------
# FEATURE 7 – MACRO CALCULATOR
# ------------------------------------------------------------
elif page == "Macro Calculator":

    st.title("🔥 Macro Calculator")

    weight = st.number_input("Enter Weight (kg)", 30, 120, 60)

    calories = weight * 35
    protein = weight * 1.8
    carbs = weight * 4
    fats = weight * 1

    st.write(f"Estimated Daily Calories: {calories}")
    st.write(f"Protein (g): {protein}")
    st.write(f"Carbs (g): {carbs}")
    st.write(f"Fats (g): {fats}")


# ------------------------------------------------------------
# FEATURE 8 – SESSION HISTORY
# ------------------------------------------------------------
elif page == "Session History":

    st.title("📝 AI Session Logs")

    if st.session_state.history:
        for entry in st.session_state.history:
            st.write(f"### {entry['feature']} – {entry['time']}")
            st.write(entry["output"])
            st.markdown("---")
    else:
        st.info("No sessions generated yet.")


# ------------------------------------------------------------
# FOOTER
# ------------------------------------------------------------
st.sidebar.markdown("---")
st.sidebar.caption("CoachBot AI – Advanced Version")
