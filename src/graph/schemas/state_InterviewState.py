import operator
from langgraph.graph import MessagesState
from typing import Annotated
from graph.schemas.schema_analysts import Analyst

class InterviewState(MessagesState):
    max_num_turns: int # Number turns of conversation
    context: Annotated[list, operator.add] # Source docs
    analyst: Analyst # Analyst asking questions
    interview: str # Interview transcript
    sections: list # Final key we duplicate in outer state for Send() API