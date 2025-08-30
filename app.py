import streamlit as st

from dotenv import load_dotenv

from src.core.planner import TravelPlanner


# Page text content:
st.set_page_config(page_title="AI Travel Planner")
st.title("AI Travel Itinerary Planner")
st.write(
    "Plan your trip itinerary by entering the trip duration (number of days), destination city, \
and interests."
)

load_dotenv()

with st.form("planner_form"):
    n_days = st.text_input("Enter the trip duration (number of days):")
    city = st.text_input("Enter the destination city name:")
    interests = st.text_input(
        "Enter your (comma-separated) interests in the destination city:"
    )
    submitted = st.form_submit_button("Generate itinerary")

    if submitted:
        if n_days and city and interests:
            planner = TravelPlanner()
            planner.set_n_days(n_days)
            planner.set_city(city)
            planner.set_interests(interests)
            itinerary = planner.create_itinerary()

            st.subheader("📄 Your Custom Itinerary:")
            st.markdown(itinerary)
        else:
            st.warning("Please enter values for all above fields")
