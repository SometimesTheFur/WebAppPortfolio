from PIL import Image
import json
import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Timothy Mahr", page_icon=":rocket:", layout="wide")


def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# ----USE LOCAL CSS----
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# ----LOAD ASSETS----
animation1 = load_lottieurl("https://assets10.lottiefiles.com/private_files/lf30_pljwgbzs.json")
image_hoverdoodle = Image.open("Images/HoverDoodle.png")
image_r_p_s = Image.open("Images/RockPaperScissors.png")

# ----HEADER----
with st.container():
    st.subheader("Hello, I'm Timothy")
    st.title("A Blossoming Developer for Networking and Cybersecurity")
    st.write(
        "Currently enrolled in the Networking and Cybersecurity degree program at Finger Lakes Community College with a focus on object-oriented programming languages and technical ethics.")  # NOQA
    st.write(
        "To check out a more in-depth portfolio, please visit: [My Google Portfolio](https://sites.google.com/view/timothymahrportfolio/about-me?authuser=0)")  # NOQA

# ----WHAT I DO----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Who I am")
        st.write("##")
        st.write(
            """
            Simply put, I am passionate about what I do.
            
            It shows through the things that I produce.
            
            Every project is an opportunity to express my gratitude and curiosity while giving me the chance to grow 
            and become stronger for what comes next.
            """
        )
with right_column:
    st_lottie(animation1, height=500, key="coding")

# ----PROJECTS----
with st.container():
    st.write("---")
    st.header("My projects")
    st.write("Some simple and fun interactive toys, puzzles, and games I've built using JS, Java, and Python")
    st.write("##")
    image_column_1, discription_column_1 = st.columns((1, 2))

    with image_column_1:
        st.image(image_r_p_s)
    with discription_column_1:
        st.subheader("Rock, Paper, Scissors")
        st.write("The classic project written entirely in JS!")
        st.write("[PLAY](https://sites.google.com/view/timothymahrportfolio/projects/rock-paper-scissors-game?authuser=0)") # NOQA

with st.container():
    st.write("##")
    image_column_2, discription_column_2 = st.columns((1, 2))

    with image_column_2:
        st.image(image_hoverdoodle)
    with discription_column_2:
        st.subheader("Hover Doodle")
        st.write("A fun toy that I made in hopes to reimagine the Etch-a-Sketch")
        st.write("[PLAY](https://sites.google.com/view/timothymahrportfolio/projects/hover-doodle?authuser=0)")


# ----CONTACT----
with st.container():
    st.write("---")
    st.subheader("Get in touch!")
    st.write("##")
    contact_form = """
                <form action="https://formsubmit.co/timothymahr@gmail.com" method="POST">
                    <input type="hidden" name="_captcha" value="false">
                    <input type="text" name="name" placeholder="Your Name" required>
                    <input type="email" name="email" placeholder="Your Email" required>
                    <textarea name="message" placeholder="Your Message Here" required></textarea>
                    <button type="submit">Send</button>
                </form>
                """
    left_column_3, right_column_3 = st.columns(2)
    with left_column_3:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column_3:
        st.empty()

