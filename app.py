import streamlit as st
import random

st.set_page_config(page_title=" Guess the Number Game 🎲", page_icon="🎲")

# Initialize session state
if "secret_number" not in st.session_state:
    st.session_state.secret_number = random.randint(1, 10)
if "attempts" not in st.session_state:
    st.session_state.attempts = 0

st.title("Guess the Number Game 🎲")

st.write("I'm thinking of a number between 1 and 10. Can you guess it?")

guess = st.number_input("Enter your guess:", min_value=1, max_value=10, step=1)

if st.button("Guess"):
    st.session_state.attempts += 1
    if guess == st.session_state.secret_number:
        st.success(f"Congratulations! You guessed it in {st.session_state.attempts} tries 🎉.")
    elif guess < st.session_state.secret_number:
        st.warning("Oops, your guess is too low. Try again!")
    else:
        st.warning("Oops, your guess is too high. Try again!")

if st.button("Reset Game"):
    st.session_state.secret_number = random.randint(1, 10)
    st.session_state.attempts = 0
    st.success("Game has been reset! Guess a new number.")
