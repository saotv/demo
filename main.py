import streamlit as st
import game1

# Set the page config
st.set_page_config(page_title="Game Center", layout="wide")

# Page navigation
st.sidebar.title('Navigation')
selection = st.sidebar.radio("Go to", ['Home', 'Guess the Number Game', 'Game 2', 'Game 3'])

if selection == 'Home':
    st.title("Welcome to the Game Center")
    st.write("Please select a game from the navigation menu.")
elif selection == 'Guess the Number Game':
    game1.show_game()
# elif selection == 'Game 2':
    # Call your game 2 function here
# elif selection == 'Game 3':
    # Call your game 3 function here