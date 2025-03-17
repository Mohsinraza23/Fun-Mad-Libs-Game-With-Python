import streamlit as st
import random

# Streamlit App Title
st.title("🎭 Fun Mad Libs Game!")

# Sidebar for User Inputs
st.sidebar.header("Fill in the Blanks ✍️")

# Taking User Inputs
adj = st.sidebar.text_input("Enter an Adjective:", "amazing")
verb1 = st.sidebar.text_input("Enter a Verb:", "code")
verb2 = st.sidebar.text_input("Enter another Verb:", "create")
famous_person = st.sidebar.text_input("Enter a Famous Person:", "Elon Musk")

# Fun Sentences to Make it More Interesting
madlib_templates = [
    f"Computer programming is so {adj}! It makes me so excited all the time because I love to {verb1}. Stay hydrated and {verb2} like you are {famous_person}!",
    f"The world of AI is {adj}! Every day, I wake up and {verb1}, hoping to {verb2} like {famous_person}.",
    f"Success is {adj}. If you want to be like {famous_person}, you must {verb1} every day and never forget to {verb2}!"
]

# Button to Generate Mad Libs
if st.button("Generate Mad Lib 🎭"):
    selected_madlib = random.choice(madlib_templates)
    st.subheader("Here's Your Mad Lib! 🎉")
    st.write(selected_madlib)

# Footer
st.markdown("Made with ❤️ by Mohsin Raza")
