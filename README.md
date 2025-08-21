
🚀 # SME Business Coach Crew

The SME Business Coach Crew is an AI-powered multi-agent system powered by [crewAI](https://crewai.com) designed to help small and medium-sized businesses (SMEs) in Nigeria grow, stay compliant, and operate more effectively.

🔍 What It Does

Provides growth and marketing strategies tailored for Nigerian SMEs.

Guides informal businesses on compliance and registration basics (CAC, tax, levies).

Compiles all insights into a single SME Growth & Compliance Report.

⚙️ How It Works

This crew is made up of 3 specialized AI agents:

SME Business Coach – gives advice on business growth, record-keeping, and digital tools.

Informal Compliance Helper – simplifies CAC registration and compliance processes for informal traders.

Business Aggregator – organizes everything into a structured SME Growth & Compliance Plan.

📝 Output

The system produces a Markdown report with sections on:

Business Growth Recommendations

Compliance & Registration Steps

Digital Tools for Nigerian SMEs

## Installation

Ensure you have Python >=3.10 <3.14 installed on your system. This project uses [UV](https://docs.astral.sh/uv/) for dependency management and package handling, offering a seamless setup and execution experience.

First, if you haven't already, install uv:

```bash
pip install uv
```

Next, navigate to your project directory and install the dependencies:

(Optional) Lock the dependencies and install them by using the CLI command:
```bash
crewai install
```
## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the sme-business-coach Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will run the create a `report.md` file with the output of a research on LLMs in the root folder.

## Streamlit Demo

Run an interactive demo UI with Streamlit:

1. Ensure your OpenAI key is available (either in a `.env` file or environment):

```bash
echo OPENAI_API_KEY=your_key_here > .env
```

2. Install dependencies (using uv or pip):

```bash
# Using uv
uv sync

# Or using pip
pip install -e .
```

3. Launch the app:

```bash
streamlit run streamlit_app.py
```

4. Enter your business/topic description and click "Generate Plan". The app will run the crew and display the output. If a `report.md` file is produced, it will also be rendered in the app.
