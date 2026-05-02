#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from stock_picker_agent.crew import StockPickerAgent

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the StockPicker crew.
    """
    inputs = {
        'sector': 'Automotive',
        'current_year': str(datetime.now().year)
    }

    try:
        result = StockPickerAgent().crew().kickoff(inputs=inputs)

        print("========== Stock Picker Result: ==========")
        print(result)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")
