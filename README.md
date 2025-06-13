---
title: topic_researcher
app_file: app.py
sdk: gradio
sdk_version: 5.33.1
---
# TopicResearcher Crew

Welcome to the TopicResearcher Crew project, powered by [crewAI](https://crewai.com). This template is designed to help you set up a multi-agent AI system with ease, leveraging the powerful and flexible framework provided by crewAI. Our goal is to enable your agents to collaborate effectively on complex tasks, maximizing their collective intelligence and capabilities.

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

### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

- Modify `src/topic_researcher/config/agents.yaml` to define your agents
- Modify `src/topic_researcher/config/tasks.yaml` to define your tasks
- Modify `src/topic_researcher/crew.py` to add your own logic, tools and specific args
- Modify `src/topic_researcher/main.py` to add custom inputs for your agents and tasks

## Running the Project

### Web Interface
The project now includes a Gradio web interface for interactive topic research. To launch it:

```bash
$ crewai run
```

This will start a local web server where you can:
- Enter any topic you want to research
- Get both a detailed research report and a quick summary
- View example topics for inspiration

### Command Line Usage
You can also use the project through the command line with various options:

```bash
# Train the crew for a specific number of iterations
$ crewai train <iterations> <filename>

# Replay the crew execution from a specific task
$ crewai replay <task_id>

# Test the crew execution
$ crewai test <iterations> <eval_llm>
```

## Output
The project generates two types of outputs:
- A comprehensive research report (`output/report.md`)
- A concise email summary (`output/email_summary.md`)

## Understanding Your Crew

The topic_researcher Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

## Support

For support, questions, or feedback regarding the TopicResearcher Crew or crewAI.
- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.
