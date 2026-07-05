from graph.schemas.state_InterviewState import InterviewState
from langchain_core.messages import HumanMessage, SystemMessage
from config.model import get_llm
# import section_writer_instructions
from graph.write.section_writer_instructions import section_writer_instructions

def write_section(state: InterviewState):

    """ Node to write a section """

    # Get state
    interview = state["interview"]
    context = state["context"]
    analyst = state["analyst"]
    llm = get_llm()
   
    # Write section using either the gathered source docs from interview (context) or the interview itself (interview)
    system_message = section_writer_instructions.format(focus=analyst.description)
    section = llm.invoke([SystemMessage(content=system_message)]+[HumanMessage(content=f"Use this source to write your section: {context}")]) 
                
    # Append it to state
    return {"sections": [section.content]}