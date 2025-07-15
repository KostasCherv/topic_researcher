from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from crewai_tools import (
    SerperDevTool,
    WebsiteSearchTool,
)


search_tool = SerperDevTool()
web_rag_tool = WebsiteSearchTool()


@CrewBase
class NewsResearcher:
    """News Researcher crew for real-time news aggregation and analysis"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def news_aggregator(self) -> Agent:
        return Agent(
            config=self.agents_config["news_aggregator"],
            tools=[search_tool, web_rag_tool],
            verbose=True,
        )

    @agent
    def sentiment_analyzer(self) -> Agent:
        return Agent(
            config=self.agents_config["sentiment_analyzer"],
            tools=[search_tool, web_rag_tool],
            verbose=True,
        )

    @agent
    def trend_spotter(self) -> Agent:
        return Agent(
            config=self.agents_config["trend_spotter"],
            tools=[search_tool, web_rag_tool],
            verbose=True,
        )

    @agent
    def fact_checker(self) -> Agent:
        return Agent(
            config=self.agents_config["fact_checker"],
            tools=[search_tool, web_rag_tool],
            verbose=True,
        )

    @agent
    def impact_assessor(self) -> Agent:
        return Agent(
            config=self.agents_config["impact_assessor"],
            tools=[search_tool, web_rag_tool],
            verbose=True,
        )

    @agent
    def crisis_monitor(self) -> Agent:
        return Agent(
            config=self.agents_config["crisis_monitor"],
            tools=[search_tool, web_rag_tool],
            verbose=True,
        )

    @agent
    def summary_generator(self) -> Agent:
        return Agent(
            config=self.agents_config["summary_generator"],
            verbose=True,
        )

    @task
    def news_aggregation_task(self) -> Task:
        return Task(
            config=self.tasks_config["news_aggregation_task"],
        )

    @task
    def sentiment_analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config["sentiment_analysis_task"],
        )

    @task
    def trend_analysis_task(self) -> Task:
        return Task(
            config=self.tasks_config["trend_analysis_task"],
        )

    @task
    def fact_checking_task(self) -> Task:
        return Task(
            config=self.tasks_config["fact_checking_task"],
        )

    @task
    def impact_assessment_task(self) -> Task:
        return Task(
            config=self.tasks_config["impact_assessment_task"],
        )

    @task
    def crisis_monitoring_task(self) -> Task:
        return Task(
            config=self.tasks_config["crisis_monitoring_task"],
        )

    @task
    def news_summary_task(self) -> Task:
        return Task(
            config=self.tasks_config["news_summary_task"],
            output_file="output/news_summary.md",
        )

    @crew
    def crew(self) -> Crew:
        """Creates the News Researcher crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
