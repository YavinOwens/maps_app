import streamlit as st 
import pandas as pd
import plotly as px



def load_data(data):
    return pd.read_csv(data)

def main():

    st.title("maps app")
    menu = ["Home", "Advanced", "Attendees", "About"]

    choice = st.sidebar.selectbox("Menu", menu)

    if choice == "Home":
        world = load_data("worldcities.csv")
        with st.expander("Data View"):
            st.dataframe(world)

    fig = px.
    if choice == "Advanced":
        pass
    if choice == "Attendees":
        pass
    if choice == "About":
        pass





if __name__ == "__main__":
    main()