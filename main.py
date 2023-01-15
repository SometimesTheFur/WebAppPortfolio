import streamlit as st

st.set_page_config(page_title="Timothy Mahr", page_icon=":rocket:", layout="wide")

# ----HEADER----
with st.container():
    st.subheader("Hello, I'm Timothy")
    st.title("A Blossoming Developer for Networking and Cybersecurity")
    st.write("Currently enrolled in the Networking and Cybersecurity degree program at Finger Lakes Community College with a focus on object-oriented programming languages and technical ethics.") # NOQA
    st.write("For more info, please visit: [My Google Portfolio](https://sites.google.com/view/timothymahrportfolio/about-me?authuser=0)") # NOQA

# ----WHAT I DO----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("What I do")
        st.write("##")
        st.write(
            """
            I am the rare Gen 'Y' stuck between Millennials and Gen 'X'.
            - I spent my teens listening to Sonic Youth, David Bowie and Skipping school to watch David Lynch and John Waters Films in the Theatre.
            - In my 20's I was often a starving artist listening to Sonic Youth, David Bowie and GodSpeed! You Black Emperor.
            - My 30's were spent in the NYC media circus.
            - Now, I'm 42 and in the Hudson Valley going to Online College to learn Cybersecurity and kick virtual bad-guys butts!
            
            But seriously, I love nature and our planet and my dog and my family and making music and coding and karate and climbing.
            Not always in that order!
            """
        )


