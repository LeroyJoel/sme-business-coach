import os
from datetime import datetime
import time

import streamlit as st
from dotenv import load_dotenv

# Try different import paths
try:
    from sme_business_coach.crew import SmeBusinessCoach
except ImportError:
    try:
        from src.sme_business_coach.crew import SmeBusinessCoach
    except ImportError:
        # If running from the project root, try direct import
        import sys
        sys.path.append(os.path.dirname(os.path.abspath(__file__)))
        from crew import SmeBusinessCoach

def initialize_environment() -> None:
    load_dotenv()
    # Check for Gemini API key (common names)
    gemini_key = (os.getenv("GEMINI_API_KEY") or 
                  os.getenv("GOOGLE_API_KEY") or 
                  os.getenv("GOOGLE_GEMINI_API_KEY"))
    
    if not gemini_key:
        st.error("⚠️ Gemini API Key not found. Please set one of these in your .env file:")
        st.code("""
GEMINI_API_KEY=your_key_here
# OR
GOOGLE_API_KEY=your_key_here
# OR  
GOOGLE_GEMINI_API_KEY=your_key_here
        """)
        st.stop()

def run_crew(business_description: str) -> str:
    inputs = {
        "business_description": business_description,
        "current_year": str(datetime.now().year),
    }
    try:
        result = SmeBusinessCoach().crew().kickoff(inputs=inputs)
        if isinstance(result, str):
            return result
        if hasattr(result, 'raw'):
            return str(result.raw)
        # Fallback: read report.md if generated
        report_path = os.path.join(os.getcwd(), "report.md")
        if os.path.exists(report_path):
            with open(report_path, "r", encoding="utf-8") as f:
                return f.read()
        return "Run completed, but no textual result was returned."
    except Exception as exc:
        return f"Error during crew run: {exc}"

def main() -> None:
    st.set_page_config(
        page_title="Nigerian SME Business Coach",
        page_icon="🇳🇬",
        layout="wide",
        initial_sidebar_state="collapsed"
    )
    
    initialize_environment()

    # Custom CSS for better styling
    st.markdown("""
    <style>
    .main-header {
        background: linear-gradient(90deg, #00804b 0%, #008751 100%);
        padding: 2rem 0;
        margin: -1rem -1rem 2rem -1rem;
        color: white;
        text-align: center;
        border-radius: 0 0 20px 20px;
    }
    .feature-card {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #00804b;
        margin: 1rem 0;
    }
    .example-card {
        background: #fff3cd;
        padding: 1rem;
        border-radius: 8px;
        border: 1px solid #ffeaa7;
        margin: 0.5rem 0;
        cursor: pointer;
        transition: all 0.3s ease;
    }
    .example-card:hover {
        background: #fff8e1;
        transform: translateY(-2px);
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    .stButton > button {
        width: 100%;
        background: linear-gradient(90deg, #00804b 0%, #008751 100%);
        color: white;
        border: none;
        padding: 0.75rem 1rem;
        border-radius: 8px;
        font-weight: 600;
    }
    .stButton > button:hover {
        background: linear-gradient(90deg, #006d3f 0%, #007344 100%);
        transform: translateY(-1px);
    }
    </style>
    """, unsafe_allow_html=True)

    # Header Section
    st.markdown("""
    <div class="main-header">
        <h1>🇳🇬 Nigerian SME Business Coach</h1>
        <p style="font-size: 1.2rem; margin: 0; opacity: 0.9;">
            AI-Powered Growth Plans & Compliance Guidance for Nigerian Small Businesses
        </p>
    </div>
    """, unsafe_allow_html=True)

    # What You'll Get Section
    st.markdown("## 🎯 What You'll Get")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("""
        <div class="feature-card">
            <h4>📈 Growth Strategy</h4>
            <p>Tailored marketing tips, sales strategies, and digital tools recommendations specific to your business type.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="feature-card">
            <h4>📋 Compliance Guide</h4>
            <p>Step-by-step CAC registration process, tax requirements, and benefits of business formalization.</p>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown("""
        <div class="feature-card">
            <h4>🛠️ Action Plan</h4>
            <p>Practical, actionable steps you can implement immediately to grow your business.</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")

    # Input Section
    st.markdown("## 📝 Tell Us About Your Business")
    st.markdown("Be as specific as possible about your business type, location, current challenges, and goals.")

    business_description = st.text_area(
        "Business Description",
        placeholder="Example: I run a small tailoring shop in Kano that specializes in traditional Hausa clothing. I currently work from home and take orders through WhatsApp. I want to get a physical shop, register with CAC, and reach more customers online.",
        height=150,
        max_chars=800,
        help="Include: Business type, location, what you sell/do, current challenges, and what you want to achieve."
    )

    # Quick Examples Section
    st.markdown("### 💡 Need inspiration? Try these examples:")
    
    example_col1, example_col2 = st.columns(2)
    
    with example_col1:
        if st.button("🍕 Restaurant Business"):
            st.session_state.selected_example = "I own a small restaurant in Ibadan that serves local Nigerian dishes like jollof rice, pepper soup, and grilled fish. I currently serve only walk-in customers but want to start home delivery, create social media presence, and formalize my business with CAC registration."
        
        if st.button("📱 Tech Repair Shop"):
            st.session_state.selected_example = "I run a phone and laptop repair service from a small shop in Abuja. I fix smartphones, tablets, and computers. My business is currently informal, and I want to register with CAC, get proper business insurance, and expand to sell phone accessories."
    
    with example_col2:
        if st.button("👗 Fashion Design"):
            st.session_state.selected_example = "I'm a fashion designer in Lagos creating contemporary African wear for young professionals. I currently sell through Instagram and WhatsApp but want to create an online store, participate in fashion shows, and scale my production."
        
        if st.button("🚚 Logistics Service"):
            st.session_state.selected_example = "I operate a small delivery service in Port Harcourt with two motorcycles, helping local businesses deliver products to customers. I want to formalize the business, get more clients, and eventually add a van to handle bigger deliveries."

    # Use selected example
    if 'selected_example' in st.session_state and st.session_state.selected_example:
        business_description = st.session_state.selected_example
        st.info(f"📌 Using example: {business_description[:100]}...")

    st.markdown("---")

    # Generate Plan Section
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        generate_button = st.button(
            "🚀 Generate My Business Plan",
            disabled=not business_description.strip(),
            help="Click to get your customized SME growth and compliance plan"
        )

    if generate_button and business_description.strip():
        # Progress tracking
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        # Simulate progress steps
        progress_steps = [
            (20, "🔍 Analyzing your business..."),
            (40, "📊 Researching growth strategies..."),
            (60, "📋 Checking compliance requirements..."),
            (80, "✍️ Generating your customized plan..."),
            (100, "✅ Plan ready!")
        ]
        
        with st.spinner("Our AI business coaches are working on your plan..."):
            for progress, message in progress_steps:
                progress_bar.progress(progress)
                status_text.text(message)
                time.sleep(1)
            
            result_text = run_crew(business_description.strip())

        # Clear progress indicators
        progress_bar.empty()
        status_text.empty()

        if result_text.startswith("Error during crew run:"):
            st.error(f"❌ {result_text}")
        else:
            st.success("🎉 Your customized SME business plan is ready!")
            
            # Action buttons
            col1, col2, col3 = st.columns(3)
            with col1:
                st.download_button(
                    label="📄 Download Plan (PDF-ready)",
                    data=result_text,
                    file_name=f"Nigerian_SME_Plan_{datetime.now().strftime('%Y%m%d_%H%M%S')}.md",
                    mime="text/markdown",
                    help="Download your business plan as a Markdown file"
                )
            
            with col2:
                if st.button("📧 Email This Plan", help="Copy the plan to email (coming soon)"):
                    st.info("📧 Email feature coming soon! For now, please download the plan.")
            
            with col3:
                if st.button("🔄 Generate Another Plan"):
                    st.session_state.clear()
                    st.rerun()
            
            st.markdown("---")
            st.markdown("## 📋 Your Customized Business Plan")
            st.markdown(result_text)
            
            # Feedback section
            st.markdown("---")
            st.markdown("### 💬 How was this plan?")
            feedback_col1, feedback_col2, feedback_col3 = st.columns(3)
            with feedback_col1:
                if st.button("👍 Very Helpful"):
                    st.success("Thank you for your feedback!")
            with feedback_col2:
                if st.button("👌 Somewhat Helpful"):
                    st.info("Thank you! We're always improving.")
            with feedback_col3:
                if st.button("👎 Not Helpful"):
                    st.warning("Sorry about that! Please try with more specific business details.")

    elif generate_button:
        st.warning("⚠️ Please describe your business first before generating a plan.")

    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #666; padding: 2rem 0;">
        <p>🇳🇬 Built for Nigerian entrepreneurs • Powered by AI • Made with ❤️</p>
        <p><small>This tool provides general business guidance. For legal and financial advice, consult with qualified professionals.</small></p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()