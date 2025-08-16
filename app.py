import streamlit as st
import random
from datetime import date

st.set_page_config(page_title="Burak Efe's Projects", page_icon="🚀", layout="centered")
st.title("🚀 Burak Efe's Projects")

# Sidebar: Project selection
project = st.sidebar.radio("Select a project:", 
                           ["🎲 Dice Roll", "🧮 Calculator", "🔢 Guess the Number", "🎂 Age Calculator", "📝 To Do List"])

# 1️⃣ Dice Roll
if project == "🎲 Dice Roll":
    st.header("🎲 Dice Roll")
    if st.button("Roll the Dice"):
        dice = random.randint(1, 6)
        st.success(f"You rolled: {dice}")

# 2️⃣ Calculator
elif project == "🧮 Calculator":
    st.header("🧮 Calculator")
    num1 = st.number_input("Enter first number", value=0.0)
    num2 = st.number_input("Enter second number", value=0.0)
    operator = st.selectbox("Select an operator", ["+", "-", "*", "/"])
    if st.button("Calculate"):
        if operator == "+":
            result = num1 + num2
        elif operator == "-":
            result = num1 - num2
        elif operator == "*":
            result = num1 * num2
        elif operator == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                st.error("Error: Division by zero!")
                result = None
        if result is not None:
            st.success(f"Result: {round(result, 3)}")

# 3️⃣ Guess the Number
elif project == "🔢 Guess the Number":
    st.header("🔢 Guess the Number (1-100)")
    if "number" not in st.session_state:
        st.session_state.number = random.randint(1, 100)
        st.session_state.attempts = 5

    guess = st.number_input("Enter your guess", min_value=1, max_value=100, step=1)
    if st.button("Guess"):
        if st.session_state.attempts > 0:
            st.session_state.attempts -= 1
            if guess == st.session_state.number:
                st.success("Congratulations! Your guess is correct 🎉")
                st.session_state.number = random.randint(1, 100)
                st.session_state.attempts = 5
            elif guess < st.session_state.number:
                st.warning("Too low! Try a bigger number.")
            else:
                st.warning("Too high! Try a smaller number.")
            if st.session_state.attempts == 0:
                st.error("You have no chances left! The number was: " + str(st.session_state.number))
                st.session_state.number = random.randint(1, 100)
                st.session_state.attempts = 5

# 4️⃣ Age Calculator
elif project == "🎂 Age Calculator":
    st.header("🎂 Age Calculator")
    birth_year = st.number_input("What year were you born?", min_value=1900, max_value=date.today().year, step=1)
    current_year = st.number_input("Current year", min_value=1900, max_value=date.today().year, value=date.today().year, step=1)
    if st.button("Calculate Age"):
        age = current_year - birth_year
        st.success(f"You are {age} years old")

# 5️⃣ To Do List
elif project == "📝 To Do List":
    st.header("📝 To Do List")
    if "tasks" not in st.session_state:
        st.session_state.tasks = []

    new_task = st.text_input("Add a new task")
    if st.button("Add Task") and new_task:
        st.session_state.tasks.append(new_task)

    if st.session_state.tasks:
        st.subheader("Tasks:")
        for i, task in enumerate(st.session_state.tasks):
            if st.checkbox(task, key=i):
                st.session_state.tasks.pop(i)
                st.experimental_rerun()
