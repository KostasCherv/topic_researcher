#!/usr/bin/env python
"""
AI Research Assistant - Main Application
Provides a Gradio interface for general topic research, cryptocurrency analysis, and news research.
"""

import warnings
from datetime import datetime
import gradio as gr
import os

from src.topic_researcher.crew import TopicResearcher
from src.coin_researcher.crew import CoinResearcher
from src.news_researcher.crew import NewsResearcher

# Suppress warnings
warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def research_topic(topic: str) -> tuple[str, str]:
    """
    Run the topic research crew with the given topic.

    Args:
        topic: The topic to research

    Returns:
        Tuple of (full_report, summary)
    """
    if not topic.strip():
        return "Please enter a valid topic.", "Please enter a valid topic."

    inputs = {"topic": topic.strip(), "current_year": str(datetime.now().year)}

    try:
        TopicResearcher().crew().kickoff(inputs=inputs)

        # Read the generated files
        with open("output/report.md", "r", encoding="utf-8") as f:
            full_report = f.read()
        with open("output/email_summary.md", "r", encoding="utf-8") as f:
            summary = f.read()

        return full_report, summary
    except FileNotFoundError:
        error_msg = "Research completed but output files not found. Please try again."
        return error_msg, error_msg
    except Exception as e:
        error_msg = f"An error occurred while researching the topic: {str(e)}"
        return error_msg, error_msg


def research_coin(coin: str) -> str:
    """
    Run the coin research crew with the given cryptocurrency.

    Args:
        coin: The cryptocurrency to research

    Returns:
        Comprehensive summary of the cryptocurrency
    """
    if not coin.strip():
        return "Please enter a valid cryptocurrency name."

    inputs = {"coin": coin.strip(), "current_year": str(datetime.now().year)}

    try:
        CoinResearcher().crew().kickoff(inputs=inputs)

        # Read the generated file
        with open("output/coin_summary.md", "r", encoding="utf-8") as f:
            summary = f.read()

        return summary
    except FileNotFoundError:
        return "Research completed but output file not found. Please try again."
    except Exception as e:
        return f"An error occurred while researching the coin: {str(e)}"


def research_news(topic: str, time_span: str = "7 days") -> str:
    """
    Run the news research crew with the given topic and time span.
    
    Args:
        topic: The topic to research (e.g., "Crypto", "Ethereum", "DeFi")
        time_span: Time span for news (default: "7 days")
    
    Returns:
        Comprehensive news digest
    """
    if not topic.strip():
        return "Please enter a valid topic."

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


def create_topic_research_tab():
    """Create the General Topic Research tab."""
    with gr.TabItem("General Topic Research"):
        with gr.Row():
            with gr.Column(scale=1):
                topic_input = gr.Textbox(
                    label="Enter a topic to research",
                    placeholder="e.g., Defi and RWAs",
                    lines=2,
                )
                topic_submit_btn = gr.Button("Research Topic", variant="primary")
                gr.Examples(
                    examples=[
                        ["Defi and RWAs"],
                        ["AI in Healthcare"],
                        ["Blockchain Technology"],
                        ["Climate Change Solutions"],
                    ],
                    inputs=topic_input,
                )

        with gr.Tabs() as topic_tabs:
            with gr.TabItem("Full Research Report"):
                topic_full_report = gr.Markdown(label="Full Research Report")
            with gr.TabItem("Quick Summary"):
                topic_summary = gr.Markdown(label="Quick Summary")

        topic_submit_btn.click(
            fn=research_topic,
            inputs=topic_input,
            outputs=[topic_full_report, topic_summary],
        )


def create_coin_research_tab():
    """Create the Coin Research tab."""
    with gr.TabItem("Coin Research"):
        with gr.Row():
            with gr.Column(scale=1):
                coin_input = gr.Textbox(
                    label="Enter a cryptocurrency to research",
                    placeholder="e.g., Bitcoin, Ethereum, Solana",
                    lines=2,
                )
                coin_submit_btn = gr.Button("Research Coin", variant="primary")
                gr.Examples(
                    examples=[
                        ["Bitcoin"],
                        ["Ethereum"],
                        ["Solana"],
                        ["Cardano"],
                        ["Polkadot"],
                    ],
                    inputs=coin_input,
                )

        with gr.Tabs() as coin_tabs:
            with gr.TabItem("Comprehensive Analysis"):
                coin_summary = gr.Markdown(label="Research Summary")

        coin_submit_btn.click(
            fn=research_coin,
            inputs=coin_input,
            outputs=coin_summary,
        )


def create_news_research_tab():
    """Create the News Research tab."""
    with gr.TabItem("News Research"):
        with gr.Row():
            with gr.Column(scale=1):
                news_topic_input = gr.Textbox(
                    label="Enter a topic to research news about",
                    placeholder="e.g., Crypto, Ethereum, DeFi, AI",
                    lines=2,
                )
                time_span_input = gr.Dropdown(
                    choices=["1 day", "3 days", "7 days", "14 days", "30 days"],
                    value="7 days",
                    label="Time span for news",
                )
                news_submit_btn = gr.Button("Research News", variant="primary")
                gr.Examples(
                    examples=[
                        ["Crypto"],
                        ["Ethereum"],
                        ["DeFi"],
                        ["AI"],
                        ["Bitcoin"],
                    ],
                    inputs=news_topic_input,
                )

        with gr.Tabs() as news_tabs:
            with gr.TabItem("News Digest"):
                news_summary = gr.Markdown(label="News Digest")

        news_submit_btn.click(
            fn=research_news,
            inputs=[news_topic_input, time_span_input],
            outputs=news_summary,
        )


def create_interface():
    """Create and return the Gradio interface."""
    with gr.Blocks(theme=gr.themes.Soft()) as interface:
        gr.Markdown("# AI Research Assistant")
        gr.Markdown("Choose a research type and get detailed results using AI agents.")

        with gr.Tabs() as tabs:
            create_topic_research_tab()
            create_coin_research_tab()
            create_news_research_tab()

    return interface


def run():
    """Run the Gradio interface."""
    # Ensure output directory exists
    os.makedirs("output", exist_ok=True)

    interface = create_interface()
    interface.launch()


if __name__ == "__main__":
    run()
