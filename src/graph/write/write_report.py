from graph.schemas.state_ResearchGraphState import ResearchGraphState
from graph.write.report_writer_instructions import report_writer_instructions
# import report_writer_instructions
from langchain_core.messages import SystemMessage, HumanMessage
from config.model import get_llm

def write_report(state: ResearchGraphState):

    """ Node to write the final report body """

    # Full set of sections
    sections = state["sections"]
    topic = state["topic"]

    # Concat all sections together
    formatted_str_sections = "\n\n".join([f"{section}" for section in sections])
    
    # Summarize the sections into a final report
    llm = get_llm()
    system_message = report_writer_instructions.format(topic=topic, context=formatted_str_sections)    
    report = llm.invoke([SystemMessage(content=system_message)]+[HumanMessage(content=f"Write a report based upon these memos.")]) 
    return {"content": report.content}