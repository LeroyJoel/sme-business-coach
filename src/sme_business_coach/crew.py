from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
# If you want to run a snippet of code before or after the crew starts,
# you can use the @before_kickoff and @after_kickoff decorators
# https://docs.crewai.com/concepts/crews#example-crew-class-with-decorators

@CrewBase
class SmeBusinessCoach():
    """SmeBusinessCoach crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

# Agents are the individual members of your crew. They can be used to perform specific tasks, or to represent different roles within your crew.
    @agent
    def sme_business_coach(self) -> Agent:
        return Agent(
            config=self.agents_config['sme_business_coach'], # type: ignore[index]
            verbose=True
        )

    @agent
    def informal_compliance_helper(self) -> Agent:
        return Agent(
            config=self.agents_config['informal_compliance_helper'], # type: ignore[index]
            verbose=True
        )
    
    @agent
    def business_aggregator(self) -> Agent:
        return Agent(
            config=self.agents_config['business_aggregator'], # type: ignore[index]
            verbose=True
        )
    
# tasks are the actions that your crew will perform. They can be used to define workflows, processes, or any other task that your crew needs to accomplish.
    @task
    def sme_business_coach_task(self) -> Task:
        return Task(
            config=self.tasks_config['sme_business_coach_task'], # type: ignore[index]
        )
    
    @task
    def informal_compliance_helper_task(self) -> Task:
        return Task(
            config=self.tasks_config['informal_compliance_helper_task'], # type: ignore[index]
        )

    @task
    def business_aggregator_task(self) -> Task:
        return Task(
            config=self.tasks_config['business_aggregator_task'], # type: ignore[index]
            output_file='report.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the SmeBusinessCoach crew"""
    
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
