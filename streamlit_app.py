import os
from datetime import datetime

import streamlit as st
from dotenv import load_dotenv

from src.sme_business_coach.crew import SmeBusinessCoach


def initialize_environment() -> None:
    load_dotenv()
    sidebar_api_key = st.sidebar.text_input(
        "OpenAI API Key",
        value=os.getenv("OPENAI_API_KEY", ""),
        type="password",
        help="Set here for this session or use a .env file",
    )
    if sidebar_api_key:
        os.environ["OPENAI_API_KEY"] = sidebar_api_key


def run_crew(topic: str) -> str:
    inputs = {
        "topic": topic,
        "current_year": str(datetime.now().year),
    }
    try:
        result = SmeBusinessCoach().crew().kickoff(inputs=inputs)
        # crewAI often returns a string-like result from the final task
        if isinstance(result, str):
            return result
        # Fallback: read report.md if generated
        report_path = os.path.join(os.getcwd(), "report.md")
        if os.path.exists(report_path):
            with open(report_path, "r", encoding="utf-8") as f:
                return f.read()
        return "Run completed, but no textual result was returned."
    except Exception as exc:
        return f"Error during crew run: {exc}"


def main() -> None:
    st.set_page_config(page_title="Nigeria SME Business Coach", layout="wide")
    initialize_environment()

    st.title("Nigeria SME Business Coach (crewAI)")
    st.write(
        "Get a tailored SME growth plan and compliance guidance for Nigerian businesses."
    )

    topic = st.text_input(
        "Describe your business or topic (e.g., 'Lagos retail shop expanding online')",
        value="AI LLMs",
        max_chars=300,
    )

    run_button = st.button("Generate Plan", type="primary")

    if run_button:
        if not os.getenv("OPENAI_API_KEY"):
            st.error("OPENAI_API_KEY is not set. Provide it in the sidebar or .env.")
            return

        with st.spinner("Running SME Business Coach... this may take a moment"):
            result_text = run_crew(topic)

        if result_text.startswith("Error during crew run:"):
            st.error(result_text)
        else:
            st.success("Completed!")
            st.markdown(result_text)


if __name__ == "__main__":
    main()


