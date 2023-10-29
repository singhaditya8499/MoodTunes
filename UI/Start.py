import streamlit as st

st.title("MoodTunes")
st.subheader("Hello, start by filling in the details below")

# Define the list of symptoms with their descriptions
symptoms = [
    ("Anxious Mood", "Worries, anticipation of the worst, fearful anticipation, irritability"),
    ("Tension", "Feelings of tension, fatigability, startle response, moved to tears easily, trembling, feelings of restlessness, inability to relax"),
    ("Fears", "Of dark, of strangers, of being left alone, of animals, of traffic, of crowds"),
    ("Insomnia", "Difficulty in falling asleep, broken sleep, unsatisfying sleep and fatigue on waking, dreams, nightmares, night terrors"),
    ("Intellectual", "Difficulty in concentration, poor memory"),
    ("Depressed Mood", "Loss of interest, lack of pleasure in hobbies, depression, early waking, diurnal swing"),
    ("Somatic (Muscular)", "Pains and aches, twitching, stiffness, myoclonic jerks, grinding of teeth, unsteady voice, increased muscular tone"),
    ("Somatic (Sensory)", "Tinnitus, blurring of vision, hot and cold flushes, feelings of weakness, pricking sensation"),
    ("Cardiovascular Symptoms", "Tachycardia, palpitations, pain in chest, throbbing of vessels, fainting feelings, missing beat"),
    ("Respiratory Symptoms", "Pressure or constriction in chest, choking feelings, sighing, dyspnea"),
    ("Gastrointestinal Symptoms", "Difficulty in swallowing, wind abdominal pain, burning sensations, abdominal fullness, nausea, vomiting, borborygmi, looseness of bowels, loss of weight, constipation"),
    ("Genitourinary Symptoms", "Frequency of micturition, urgency of micturition, amenorrhea, menorrhagia, development of frigidity, premature ejaculation, loss of libido, impotence"),
    ("Autonomic Symptoms", "Dry mouth, flushing, pallor, tendency to sweat, giddiness, tension headache, raising of hair"),
    ("Behavior at Interview", "Fidgeting, restlessness or pacing, tremor of hands, furrowed brow, strained face, sighing or rapid respiration, facial pallor, swallowing, etc"),
]


if "sum_of_sliders" not in st.session_state:
    st.session_state["sum_of_sliders"] = 0.0
else:
    st.session_state["sum_of_sliders"] = 0.0

form_submitted = False
def calculateAnxiety():
    print()

with st.form("ham_a_form", clear_on_submit=False):
    st.markdown("##### Please rate the following symptoms on a scale of 0 to 4, where 0 is no symptoms and 4 is severe symptoms.")

    for symptom_name, symptom_description in symptoms:
        st.markdown(symptom_name)
        slider_value = st.slider(symptom_description, min_value=0, max_value=4)
        st.session_state["sum_of_sliders"] += slider_value

    submit = st.form_submit_button("Submit this form", on_click=calculateAnxiety)
    form_submitted = True if submit else form_submitted

if form_submitted:
    st.write("Sum of slider values:", st.session_state.sum_of_sliders)
    st.write("Thank you for submitting the form!")





