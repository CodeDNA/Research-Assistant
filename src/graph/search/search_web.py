from graph.schemas.state_InterviewState import InterviewState
from graph.schemas.schema_searchQuery import SearchQuery
from langchain_tavily import TavilySearch
from config.model import get_llm
# import search_instructions
from graph.search.search_instructions import search_instructions

def search_web(state: InterviewState):
    
    """ Retrieve docs from web search """

    # LLM
    llm = get_llm()
    # Search
    tavily_search = TavilySearch(max_results=3)

    # Search query
    structured_llm = llm.with_structured_output(SearchQuery)
    search_query = structured_llm.invoke([search_instructions]+state['messages'])
    
    # Search
    data = tavily_search.invoke({"query": search_query.search_query})
    search_docs = data.get("results", data)

     # Format
    formatted_search_docs = "\n\n---\n\n".join(
        [
            f'<Document href="{doc["url"]}"/>\n{doc["content"]}\n</Document>'
            for doc in search_docs
        ]
    )

    return {"context": [formatted_search_docs]} 