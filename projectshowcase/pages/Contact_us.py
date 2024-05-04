import streamlit as st
st.header("Contact us")
with st.form(key="email_forms"):
    user_email = st.text_input("Your email address")
    message = st.text_area("Your Message")
    message = message + "\n" + user_email
    button = st.form_submit_button("Submit")
    if button:
        st.info(message)


