import streamlit as st

#
st.set_page_config(page_title="Website App", page_icon=":tada:",layout="wide")
with st.container():
    st.subheader("Hi, this is Onik :wave:")
    st.title("Computer science student")
    st.write("Coding id fun!?")
    st.write("[LinkedIn>](https://www.linkedin.com/in/onikahmed)")
with st.container():
    st.write("---")
    left_column, middle_column, middle1_column, right_column = st.columns(4)
    with left_column:
        st.header("Column 1")
        st.write("##")
        st.write("This is a Test")
    with right_column:
        st.header("Column 2")
    with middle_column:
        st.header("Column 3")
    with middle1_column:
        st.header("Column 4")
        clicked=st.button("Hi")
        if clicked:
            st.write("hello")

with st.container():
    st.write("---")