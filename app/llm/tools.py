from langchain.tools import tool
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_core.runnables.config import RunnableConfig

@tool
def web_search_tool(query: str, config: RunnableConfig):
    """ Use this tool to search for information on the internet """

    web_search = TavilySearchResults(max_results=10)

    return web_search.invoke({'query': query})
