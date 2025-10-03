from crew.agents.agents_trends import *
from crew.tasks.task_trends import *
from crewai import Crew

crew = Crew(
    agents=[research, review, trends],
    tasks=[task_research, task_review, task_trends]
)