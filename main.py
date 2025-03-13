import streamlit as st
import random
import string


def passwgen(length, use_int, use_special):
    characters = string.ascii_letters  # all letters

    if use_int:
        characters += string.digits  # add numbers

    if use_special:
        characters += string.punctuation  # add special characters ( !, @, #, etc.)

    return "".join(random.choice(characters) for _ in range(length))


# streamlit
st.set_page_config(page_title="Password Generator", page_icon="🔒")
st.title("🔒 Password Generator ")

length = st.slider("Length of password", min_value=5, max_value=50, value=10)
use_int = st.checkbox("Use Numbers 🔢")
use_special = st.checkbox("Use Special Characters")

if "password" not in st.session_state:
    st.session_state.password = ""

if st.button("Generate Password 🧬"):
    st.session_state.password = passwgen(length, use_int, use_special)
    st.success("Password Has Been Generated Successfully ✅")
    st.write("""## Copy your Generated Password 🔽""")
    st.code(st.session_state.password,language=None)

if st.session_state.password:
    st.markdown(
        "[Check Strenght of your Generated Password 💪](https://aliyan-password-strength.streamlit.app/)"
    )
st.write("Made with ❤️ by Aliyan Jabbar")
