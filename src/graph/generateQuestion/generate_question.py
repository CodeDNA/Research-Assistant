from graph.schemas.state_InterviewState import InterviewState
from graph.generateQuestion.question_instructions import question_instructions
# import question_instructions
from langchain_core.messages import SystemMessage
from config.model import get_llm


def generate_question(state: InterviewState):

    """ Node to generate a question """

    # Get state
    analyst = state["analyst"]
    messages = state["messages"]

    # Generate question 
    llm = get_llm()
    system_message = question_instructions.format(goals=analyst.persona)
    question = llm.invoke([SystemMessage(content=system_message)]+messages)
        
    # Write messages to state
    return {"messages": [question]}