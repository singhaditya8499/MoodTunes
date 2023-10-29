import streamlit as st
import pandas as pd

st.title("MoodTunes")
st.markdown("### Songs Recommendation")

# Mild - 0 -> 17 (0 - 30%) —> Suggest Happy
# Moderate - 18 -> 30 -> (30% - 54%) —--> Sad (close to 50%) and Relaxed [Sad -> Relaxed -> Happy] 
# Severe - 30 -> 56 -> (54% - 100%) —---> [Sad/Angry that is close to their severity -> Relaxed -> Happy]

clicked = False

### Angry = 0, Happy = 1, Relaxed = 2, Sad = 3

def getDataFrameMild(df, x):
    data = pd.DataFrame()
    for i in range(df.shape[0]):
        if df.iloc[i]["percentage"][1] > 0.4 or df.iloc[i]["percentage"][2] > 0.4:
            data = pd.concat([data, pd.DataFrame([df.iloc[i]])], ignore_index=True)

    data = data[['song_name', "cleaned_lyrics"]]
    shuffled_df = data.sample(frac=1.0, random_state=1)
    return shuffled_df

def getDataFrameMod(df, x):
    data_sad = pd.DataFrame()
    data_relaxed = pd.DataFrame()
    data_happy = pd.DataFrame()
    data = pd.DataFrame()
    for i in range(df.shape[0]):
        if df.iloc[i]["percentage"][3] <= x:
            if df.iloc[i]["percentage"][3] >= df.iloc[i]["percentage"][2] and df.iloc[i]["percentage"][3] >= df.iloc[i]["percentage"][1]:
                data_sad = pd.concat([data_sad, pd.DataFrame([df.iloc[i]])], ignore_index=True)
        elif df.iloc[i]["percentage"][2] >=x:
            if df.iloc[i]["percentage"][2] >= df.iloc[i]["percentage"][1] and df.iloc[i]["percentage"][2] >= df.iloc[i]["percentage"][3]:
                data_relaxed = pd.concat([data_relaxed, pd.DataFrame([df.iloc[i]])], ignore_index=True)
        elif df.iloc[i]["percentage"][1] >= x:
            if df.iloc[i]["percentage"][1] >= df.iloc[i]["percentage"][2] and df.iloc[i]["percentage"][1] >= df.iloc[i]["percentage"][3]:
                data_happy = pd.concat([data_happy, pd.DataFrame([df.iloc[i]])], ignore_index=True)

    data_sad = data_sad.sample(frac=1.0, random_state=1)
    data_relaxed = data_relaxed.sample(frac=1.0, random_state=1)
    data_happy = data_happy.sample(frac=1.0, random_state=1)
    data = pd.concat([data, data_sad], ignore_index=True)
    data = pd.concat([data, data_relaxed], ignore_index=True)
    data = pd.concat([data, data_happy], ignore_index=True)
    data = data[['song_name', 'cleaned_lyrics']]
    return data

def getDataFrameSev(df, x):
    data_sad = pd.DataFrame()
    data_relaxed = pd.DataFrame()
    data_happy = pd.DataFrame()
    data = pd.DataFrame()
    for i in range(df.shape[0]):
        if df.iloc[i]["percentage"][0] <= x or df.iloc[i]["percentage"][3] <=x:
            data_sad = pd.concat([data_sad, pd.DataFrame([df.iloc[i]])], ignore_index=True)
        elif df.iloc[i]["percentage"][2] >=x:
            data_relaxed = pd.concat([data_relaxed, pd.DataFrame([df.iloc[i]])], ignore_index=True)
        elif df.iloc[i]["percentage"][1] >= x:
            data_happy = pd.concat([data_happy, pd.DataFrame([df.iloc[i]])], ignore_index=True)

    data_sad = data_sad.sample(frac=1.0, random_state=1)
    data_relaxed = data_relaxed.sample(frac=1.0, random_state=1)
    data_happy = data_happy.sample(frac=1.0, random_state=1)
    data = pd.concat([data, data_sad], ignore_index=True)
    data = pd.concat([data, data_relaxed], ignore_index=True)
    data = pd.concat([data, data_happy], ignore_index=True)
    data = data[['song_name', 'cleaned_lyrics']]
    return data


def recommendSongs():
    global clicked  # Use the global keyword to modify the 'clicked' variable
    clicked = True
    df = pd.read_pickle("./../data/taylor_swift_data_regression_result.pkl")
    anxiety_level = st.session_state["sum_of_sliders"]
    percentage_anxiety_level = (anxiety_level)/56.0
    if percentage_anxiety_level <= 0.30:
        st.dataframe(getDataFrameMild(df, percentage_anxiety_level))
    elif percentage_anxiety_level <= 0.54:
        st.dataframe(getDataFrameMod(df, percentage_anxiety_level))
    else:
        st.dataframe(getDataFrameSev(df, percentage_anxiety_level))
    # df = df.song_name
    # st.dataframe(df, use_container_width=True)

if not clicked:
    with st.form("recommend_songs"):
        submit = st.form_submit_button("Recommend", on_click=recommendSongs)
