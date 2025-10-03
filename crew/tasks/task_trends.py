from crewai import Task
from crew.agents.agents_trends import *

task_research = Task(
    description="Busque e organize todas as informações relevantes e confiáveis disponíveis na internet sobre {tema}.",
    agent=research,
    expected_output="Um relatório detalhado com todas as informações coletadas sobre {tema}."
)

task_review = Task(
    description="Revise, corrija e refine o conteúdo produzido pelo Pesquisador sobre {tema}, destacando os pontos mais importantes.",
    agent=review,
    expected_output="Um artigo claro, coeso e revisado, com os principais pontos sobre {tema}."
)

task_trends = Task(
    description="Analise o conteúdo revisado sobre {tema} e produza insights estratégicos, destacando tendências, oportunidades e implicações relevantes.",
    agent=trends,
    expected_output="Um conjunto de insights estratégicos e recomendações práticas com base no conteúdo revisado sobre {tema}."
)
