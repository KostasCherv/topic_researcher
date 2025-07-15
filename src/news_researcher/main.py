#!/usr/bin/env python
import sys
import warnings
from datetime import datetime, timedelta
import os

from src.news_researcher.crew import NewsResearcher

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def research_news(topic: str, time_span: str = "7 days") -> str:
    """
    Run the news research crew with the given topic and time span.
    
    Args:
        topic: The topic to research (e.g., "Crypto", "Ethereum", "DeFi")
        time_span: Time span for news (default: "7 days")
    
    Returns:
        Comprehensive news digest
    """
    inputs = {
        "topic": topic.strip(), 
        "time_span": time_span,
        "current_year": str(datetime.now().year)
    }

    try:
        NewsResearcher().crew().kickoff(inputs=inputs)

        # Read the generated file
        with open("output/news_summary.md", "r", encoding="utf-8") as f:
            summary = f.read()

        return summary
    except FileNotFoundError:
        return "Research completed but output file not found. Please try again."
    except Exception as e:
        return f"An error occurred while researching the news: {str(e)}"


def run():
    """
    Run the news researcher for a specific topic.
    """
    if len(sys.argv) < 2:
        print("Usage: python main.py <topic> [time_span]")
        print("Example: python main.py 'Crypto' '7 days'")
        sys.exit(1)

    topic = sys.argv[1]
    time_span = sys.argv[2] if len(sys.argv) > 2 else "7 days"
    
    summary = research_news(topic, time_span)

    print("=== NEWS DIGEST ===")
    print(summary)


if __name__ == "__main__":
    run()
