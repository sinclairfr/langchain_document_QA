import streamlit as st

# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
         ("Standard (5-15 days)", "Express (2-5 days)")
    )
    add_yet_another_one = st.radio(
        "zooo",
        ("Standard (5-15 days)", "Express (2-5 days)")
        )