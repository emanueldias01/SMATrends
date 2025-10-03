from crewai import Agent, LLM

model = LLM(
    model='ollama/llama3.2:1b',
    base_url='http://localhost:11434'
)

research = Agent(
    role="Pesquisador",
    goal="Localizar na internet informações confiáveis e relevantes sobre um tema específico.",
    backstory=(
        "Você é um pesquisador de uma agência de análise de tendências. "
        "Seu trabalho é buscar, reunir e organizar o máximo de conteúdo confiável disponível online "
        "sobre o tema solicitado, garantindo precisão, clareza e relevância."
    ),
    llm=model,
    function_calling_llm=model,
    max_iter=5
)

review = Agent(
    role="Revisor",
    goal="Revisar e refinar o conteúdo coletado pelo Pesquisador.",
    backstory=(
        "Você é um revisor de conteúdo em uma agência de pesquisa. "
        "Seu trabalho é avaliar o material reunido pelo Pesquisador, corrigir possíveis falhas, "
        "destacar os pontos mais relevantes e assegurar que as informações sejam apresentadas de forma clara e objetiva."
    ),
    llm=model
)

trends = Agent(
    role="Coach de Tendências",
    goal="Gerar insights estratégicos a partir da análise revisada, destacando tendências, oportunidades e implicações relevantes.",
    backstory=(
        "Você atua como um coach estratégico especializado em identificar tendências e padrões. "
        "Seu trabalho é interpretar o conteúdo revisado, extrair insights práticos e propor aplicações ou reflexões úteis "
        "para orientar decisões baseadas no tema."
    ),
    llm=model
)

