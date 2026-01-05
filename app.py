import streamlit as st
from agents import WeatherAgent, ContentAgent
from pdf_utils import generate_pdf
from dotenv import load_dotenv

load_dotenv()

st.title("🌤️ Multi-Agent Weather Report Generator")

city = st.text_input("Enter City Name")

if st.button("Generate Report"):
    # Initialize Agents
    weather_agent = WeatherAgent()
    content_agent = ContentAgent()

    # Agent 1 execution
    weather_data = weather_agent.run(city)

    # Agent 2 execution
    summary = content_agent.run(weather_data)

    # Agent 3 execution (PDF)
    pdf_path = generate_pdf(summary)

    # Display Output
    st.subheader("Weather Summary")
    st.write(summary)

    with open(pdf_path, "rb") as file:
        st.download_button(
            label="📄 Download PDF Report",
            data=file,
            file_name="weather_report.pdf",
            mime="application/pdf"
        )

