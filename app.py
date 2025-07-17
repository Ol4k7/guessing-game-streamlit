import streamlit as st
import random

st.set_page_config(page_title="Guess the Number Game 🎮", layout="centered")

st.title("Guess the Number 🎲")
st.write("I'm thinking of a number between 1 and 10. Can you guess it?")

secret_number = random.randint(1, 10)
guess = st.number_input("Enter your guess:", min_value=1, max_value=10, step=1)

if st.button("Submit Guess"):
    if guess == secret_number:
        st.success("Congratulations! You guessed it right!")
    elif guess > secret_number:
        st.warning("Oops, your guess is too high!")
    else:
        st.warning("Oops, your guess is too low!")
