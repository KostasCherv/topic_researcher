#!/usr/bin/env python
import sys
import warnings
from datetime import datetime
import os

from src.coin_researcher.crew import CoinResearcher

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def research_coin(coin: str) -> tuple[str, str]:
    """
    Run the coin research crew with the given coin.
    Returns both the full knowledge base and a summary.
    """
    inputs = {"coin": coin, "current_year": str(datetime.now().year)}

    try:
        CoinResearcher().crew().kickoff(inputs=inputs)

        # Read the generated files
        with open("output/coin_knowledge_base.md", "r") as f:
            knowledge_base = f.read()

        # Create a summary from the knowledge base
        summary = f"# {coin} Research Summary\n\n"
        summary += "A comprehensive knowledge base has been generated covering:\n"
        summary += "- Executive Summary\n"
        summary += "- Tokenomics Analysis\n"
        summary += "- Market Sentiment\n"
        summary += "- On-chain Metrics\n"
        summary += "- Ecosystem Overview\n"
        summary += "- Risks & Controversies\n"
        summary += "- Recent Developments\n\n"
        summary += "Full knowledge base available in the detailed report."

        return knowledge_base, summary
    except Exception as e:
        error_msg = f"An error occurred while researching the coin: {e}"
        return error_msg, error_msg


def run():
    """
    Run the coin researcher for a specific coin.
    """
    if len(sys.argv) < 2:
        print("Usage: python main.py <coin_name>")
        sys.exit(1)

    coin = sys.argv[1]
    knowledge_base, summary = research_coin(coin)

    print("=== KNOWLEDGE BASE ===")
    print(knowledge_base)
    print("\n=== SUMMARY ===")
    print(summary)


if __name__ == "__main__":
    run()
