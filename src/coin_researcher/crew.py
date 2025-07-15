from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from crewai_tools import (
    SerperDevTool,
    WebsiteSearchTool,
)

# Initialize tools
search_tool = SerperDevTool()
web_rag_tool = WebsiteSearchTool()


@CrewBase
class CoinResearcher:
    """Coin Researcher crew for comprehensive cryptocurrency analysis"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def coin_overview_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["coin_overview_agent"],
            tools=[search_tool, web_rag_tool],
            verbose=True,
        )

    @agent
    def synthesis_agent(self) -> Agent:
        return Agent(
            config=self.agents_config["synthesis_agent"],
            verbose=True,
        )

    @agent
    def tokenomics_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config["tokenomics_analyst"],
            tools=[search_tool, web_rag_tool],
            verbose=True,
        )

    @agent
    def sentiment_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config["sentiment_analyst"],
            tools=[search_tool, web_rag_tool],
            verbose=True,
        )

    @agent
    def onchain_data_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config["onchain_data_analyst"],
            tools=[search_tool, web_rag_tool],
            verbose=True,
        )

    @agent
    def ecosystem_mapper(self) -> Agent:
        return Agent(
            config=self.agents_config["ecosystem_mapper"],
            tools=[search_tool, web_rag_tool],
            verbose=True,
        )

    @agent
    def risk_controversy_reporter(self) -> Agent:
        return Agent(
            config=self.agents_config["risk_controversy_reporter"],
            tools=[search_tool, web_rag_tool],
            verbose=True,
        )

    @agent
    def recent_developments_curator(self) -> Agent:
        return Agent(
            config=self.agents_config["recent_developments_curator"],
            tools=[search_tool, web_rag_tool],
            verbose=True,
        )

    @agent
    def market_data_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config["market_data_analyst"],
            tools=[search_tool, web_rag_tool],
            verbose=True,
        )

    @task
    def coin_overview_task(self) -> Task:
        return Task(
            config=self.tasks_config["coin_overview_task"],
        )

    @task
    def tokenomics_analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config["tokenomics_analysis_task"],
        )

    @task
    def sentiment_analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config["sentiment_analysis_task"],
        )

    @task
    def onchain_data_analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config["onchain_data_analysis_task"],
        )

    @task
    def ecosystem_mapping_task(self) -> Task:
        return Task(
            config=self.tasks_config["ecosystem_mapping_task"],
        )

    @task
    def risk_controversy_analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config["risk_controversy_analysis_task"],
        )

    @task
    def recent_developments_task(self) -> Task:
        return Task(
            config=self.tasks_config["recent_developments_task"],
        )

    @task
    def market_data_analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config["market_data_analysis_task"],
        )

    @task
    def coin_summary_task(self) -> Task:
        return Task(
            config=self.tasks_config["coin_summary_task"],
            output_file="output/coin_summary.md",
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Coin Researcher crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
