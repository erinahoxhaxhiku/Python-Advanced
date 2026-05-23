import streamlit as st
from abc import ABC, abstractmethod


# ---------------- BASE CLASS ----------------
class Person(ABC):
    def __init__(self, name, age, weight, height):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height

    @abstractmethod
    def calculate_bmi(self):
        pass

    @abstractmethod
    def get_bmi_category(self):
        pass


# ---------------- ADULT ----------------
class Adult(Person):
    def calculate_bmi(self):
        return self.weight / (self.height ** 2)

    def get_bmi_category(self):
        bmi = self.calculate_bmi()

        if bmi < 18.5:
            return "Underweight"
        elif bmi < 25:
            return "Normal weight"
        elif bmi < 30:
            return "Overweight"
        else:
            return "Obese"


# ---------------- CHILD ----------------
class Child(Person):
    def calculate_bmi(self):
        return self.weight / (self.height ** 2)

    def get_bmi_category(self):
        bmi = self.calculate_bmi()

        if bmi < 14:
            return "Underweight"
        elif bmi < 18:
            return "Normal weight"
        elif bmi < 22:
            return "Overweight"
        else:
            return "Obese"


# ---------------- STREAMLIT UI ----------------
st.set_page_config(page_title="BMI Calculator", page_icon="⚖️")

st.title("⚖️ BMI Calculator")
st.write("Enter your details below")

# Initialize session state variables if they don't exist yet
if "bmi" not in st.session_state:
    st.session_state.bmi = None
if "category" not in st.session_state:
    st.session_state.category = None

name = st.text_input("Name")
age = st.number_input("Age", min_value=1, max_value=120, step=1)
weight = st.number_input("Weight (kg)", min_value=1.0, step=0.1)
height = st.number_input("Height (m)", min_value=0.1, step=0.01)

# Clicking the button handles the logic and SAVES it to state
if st.button("Calculate BMI"):
    if name == "":
        st.error("Please enter your name")
    else:
        if age >= 18:
            person = Adult(name, age, weight, height)
        else:
            person = Child(name, age, weight, height)

        # Store the calculations in session state so they persist
        st.session_state.bmi = person.calculate_bmi()
        st.session_state.category = person.get_bmi_category()

# ---------------- DISPLAY RESULTS ----------------
# This section runs on every rerun, checking if we have saved results to show
if st.session_state.bmi is not None:
    st.markdown("---")
    st.subheader(f"Results for {name}")
    st.success(f"BMI: {st.session_state.bmi:.2f}")
    st.info(f"Category: {st.session_state.category}")