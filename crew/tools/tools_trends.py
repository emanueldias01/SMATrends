from agents import WebSearchTool
from crewai.tools import tool


@tool("web search")
def web_search():

    """
        Esta é uma ferramenta de pesquisa na web
    """
    return WebSearchTool