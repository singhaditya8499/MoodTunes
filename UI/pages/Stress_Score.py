import streamlit as st

st.title("MoodTunes")
st.subheader("Score and Interpretation")

interpretation = "Normal"
if st.session_state["sum_of_sliders"] <= 17:
    interpretation = "Mild Anxiety"
elif st.session_state["sum_of_sliders"] <= 30:
    interpretation = "Moderate Anxiety"
else:
    interpretation = "High Anxiety"

if "interpretation" not in st.session_state:
    st.session_state["interpretation"] = interpretation
else:
    st.session_state["interpretation"] = interpretation

anxiety_score = (st.session_state.sum_of_sliders*100)/56.0
interpretation1 = f"<p>{st.session_state.interpretation}</p>"
score = f"<p>{anxiety_score} %</p>"
st.markdown("##### Your anxiety category is " + interpretation1, unsafe_allow_html = True)
st.markdown("##### Your anxiety level is " + score, unsafe_allow_html = True)
