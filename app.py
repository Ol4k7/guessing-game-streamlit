import streamlit as st
import random

st.title("Guess the Secret Number !")

# Initialize secret number in session state
if 'secret_number' not in st.session_state:
    st.session_state.secret_number = random.randint(1, 10)

guess = st.number_input("Guess a number between 1 and 10", min_value=1, max_value=10, step=1)

if st.button("Submit Guess"):
    if guess == st.session_state.secret_number:
        st.success("Congratulations, you guessed it!")
        st.session_state.secret_number = random.randint(1, 10)  # Reset for next round
    elif guess > st.session_state.secret_number:
        st.info("Oops, your guess is too high!")
    else:
        st.info("Nope, your guess is too low!")

