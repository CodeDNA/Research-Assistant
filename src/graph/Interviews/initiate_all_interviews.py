from langchain_core.messages import HumanMessage
from graph.schemas.state_ResearchGraphState import ResearchGraphState
from langgraph.types import Send

def initiate_all_interviews(state: ResearchGraphState):

    """ Conditional edge to initiate all interviews via Send() API or return to create_analysts """    

    # Check if human feedback
    human_analyst_feedback=state.get('human_analyst_feedback','approve')
    if human_analyst_feedback.lower() != 'approve':
        # Return to create_analysts
        return "create_analysts"

    # Otherwise kick off interviews in parallel via Send() API
    else:
        topic = state["topic"]
        return [Send("conduct_interview", {"analyst": analyst,
                                           "messages": [HumanMessage(
                                               content=f"So you said you were writing an article on {topic}?"
                                           )
                                                       ]}) for analyst in state["analysts"]]
    