import streamlit as st

st.set_page_config(page_title="MYINFO",layout="centered")
st.title("MYINFO")

with st.form("myinfo_form"):
    name = st.text_input("Name")
    age = st.number_input("Age", min_value=0)
    gender = st.selectbox("Gender", ["Male", "Female", "Other"])
    email = st.text_input("Email")
    bio = st.text_area("Short Bio")


    submitted = st.form_submit_button("Submit")

if submitted:
    st.subheader("Here is your information:")
    st.write(f"**Name:** {name}")
    st.write(f"**Age:** {age}")
    st.write(f"**Gender:** {gender}")
    st.write(f"**Email:** {email}")
    st.write(f"**Bio:** {bio}")

else:
    st.write("Please fill out the form and click submit to see your information.")

