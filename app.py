import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

st.title("AI Travel Planner Agent")

destination = st.text_input("Destination")
budget = st.text_input("Budget")
days = st.text_input("Number of Days")

if st.button("Plan My Trip"):

    prompt = f"""
    Create a travel plan.

    Destination: {destination}
    Budget: {budget}
    Days: {days}

    Give:
    1. Day-wise itinerary
    2. Estimated expenses
    3. Travel tips
    """

    response = model.generate_content(prompt)

    st.write(response.text)
