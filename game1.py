import streamlit as st
import random

def show_game():
    st.title('Guess the Number Game')

    if 'number' not in st.session_state:
        st.session_state.number = random.randint(1, 100)
        st.session_state.attempts = 0

    guess = st.number_input('Guess a number between 1 and 100', min_value=1, max_value=100)
    submit_button = st.button('Guess')

    if submit_button:
        st.session_state.attempts += 1
        if guess < st.session_state.number:
            st.error('Too low! Try again.')
        elif guess > st.session_state.number:
            st.error('Too high! Try again.')
        else:
            st.success(f'Congratulations! You guessed it right. The number was {st.session_state.number}.')
            st.balloons()
            st.session_state.number = random.randint(1, 100)
            st.session_state.attempts = 0

    st.write(f'Number of attempts: {st.session_state.attempts}')
    if st.button('Reset Game'):
        st.session_state.number = random.randint(1, 100)
        st.session_state.attempts = 0