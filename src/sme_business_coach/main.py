#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from sme_business_coach.crew import SmeBusinessCoach

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    # Example business description for testing
    inputs = {
        'business_description': 'A small electronics repair shop in Lagos that wants to expand online and formalize their business',
        'current_year': str(datetime.now().year)
    }
    
    try:
        result = SmeBusinessCoach().crew().kickoff(inputs=inputs)
        print("Crew execution completed successfully!")
        return result
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "business_description": "A small retail clothing store in Abuja looking to improve sales and go digital",
        'current_year': str(datetime.now().year)
    }
    try:
        SmeBusinessCoach().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        SmeBusinessCoach().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "business_description": "A food truck business in Port Harcourt wanting to register with CAC and grow their customer base",
        "current_year": str(datetime.now().year)
    }
    
    try:
        SmeBusinessCoach().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

if __name__ == "__main__":
    run()