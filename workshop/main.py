import streamlit as st
import plotly.express as px
import pandas as pd



st.title("My First Streamlit App")
st.header("Hello World 👏")
st.write("This is an example of a simple Streamlit app.")



url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/refs/heads/master/glue.csv"
df = pd.read_csv(url)
st.write(df)


number = st.slider("Select a number", 0, 100, 50)
st.write("The current number is ", number)

rating = st.radio(
    "How would you rate this class?",
    ("1", "2", "3", "4", "5")
)
st.write(f"You selected {rating}")


url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/penguins.csv"

df = pd.read_csv(url)
df_grouped_by_species = df.groupby("species")["body_mass_g"].mean()
st.bar_chart(df_grouped_by_species)

fig = px.bar(df_grouped_by_species.reset_index(), x="species", y="body_mass_g")
st.plotly_chart(fig)

with st.sidebar:
    st.write("This is a sidebar")
    option = st.selectbox(
        "Which number do you like best?",
        ["1", "2", "3", "4", "5"]
    )