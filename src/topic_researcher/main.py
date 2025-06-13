#!/usr/bin/env python
import sys
import warnings
from datetime import datetime
import gradio as gr
import os

from src.topic_researcher.crew import TopicResearcher

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

topic = "Defi and RWAs"


def research_topic(topic: str) -> tuple[str, str]:
    """
    Run the topic research crew with the given topic.
    Returns both the full report and the summary.
    """
    inputs = {"topic": topic, "current_year": str(datetime.now().year)}

    try:
        TopicResearcher().crew().kickoff(inputs=inputs)

        # Read the generated files
        with open("output/report.md", "r") as f:
            full_report = f.read()
        with open("output/email_summary.md", "r") as f:
            summary = f.read()

        return full_report, summary
    except Exception as e:
        error_msg = f"An error occurred while researching the topic: {e}"
        return error_msg, error_msg


def create_interface():
    """
    Create and launch the Gradio interface.
    """
    with gr.Blocks(theme=gr.themes.Soft()) as interface:
        gr.Markdown("# Topic Researcher")
        gr.Markdown("Enter a topic and get detailed research results using AI agents.")

        with gr.Row():
            with gr.Column(scale=1):
                topic_input = gr.Textbox(
                    label="Enter a topic to research",
                    placeholder="e.g., Defi and RWAs",
                    lines=2,
                )
                submit_btn = gr.Button("Research Topic", variant="primary")
                gr.Examples(
                    examples=[
                        ["Defi and RWAs"],
                        ["AI in Healthcare"],
                        ["Blockchain Technology"],
                    ],
                    inputs=topic_input,
                )

        with gr.Tabs() as tabs:
            with gr.TabItem("Full Research Report"):
                full_report = gr.Markdown(label="Full Research Report")
            with gr.TabItem("Quick Summary"):
                summary = gr.Markdown(label="Quick Summary")

        submit_btn.click(
            fn=research_topic, inputs=topic_input, outputs=[full_report, summary]
        )

    return interface


def run():
    """
    Run the Gradio interface.
    """
    # Ensure output directory exists
    os.makedirs("output", exist_ok=True)

    interface = create_interface()
    interface.launch()


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {"topic": topic, "current_year": str(datetime.now().year)}
    try:
        TopicResearcher().crew().train(
            n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs
        )

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")


def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        TopicResearcher().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")


def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {"topic": "Defi", "current_year": str(datetime.now().year)}

    try:
        TopicResearcher().crew().test(
            n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs
        )

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")


if __name__ == "__main__":
    run()
