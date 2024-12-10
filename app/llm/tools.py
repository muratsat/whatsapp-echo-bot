from langchain.tools import tool
from langchain_community.tools.tavily_search import TavilySearchResults

@tool
def web_search_tool(query: str):
    """ Use this tool to search for information on the internet """
    tool = TavilySearchResults(
        max_results=5,
        search_depth="advanced",
        include_answer=True,
        include_raw_content=True,
        include_images=True,
    )
    
    result = tool.invoke({"query": query})

    return result
