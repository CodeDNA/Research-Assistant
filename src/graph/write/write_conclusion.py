from graph.schemas.state_ResearchGraphState import ResearchGraphState
from graph.write.intro_conclusion_instructions import intro_conclusion_instructions
# import intro_conclusion_instructions
from langchain_core.messages import HumanMessage
from config.model import get_llm

def write_conclusion(state: ResearchGraphState):

    """ Node to write the conclusion """

    # Full set of sections
    sections = state["sections"]
    topic = state["topic"]

    # Concat all sections together
    formatted_str_sections = "\n\n".join([f"{section}" for section in sections])
    
    # Summarize the sections into a final report
    llm = get_llm()
    instructions = intro_conclusion_instructions.format(topic=topic, formatted_str_sections=formatted_str_sections)    
    conclusion = llm.invoke([instructions]+[HumanMessage(content=f"Write the report conclusion")]) 
    return {"conclusion": conclusion.content}