from graph.schemas.state_InterviewState import InterviewState
from langgraph.graph import StateGraph, START, END
from graph.generateQuestion.generate_question import generate_question
from graph.search.search_web import search_web
from graph.search.search_wikipedia import search_wikipedia
from graph.generateAnswer.generate_answer import generate_answer
from graph.Interviews.save_interview import save_interview
from graph.write.write_section import write_section
from graph.routeMessages.route_messages import route_messages

# Add nodes and edges 
interview_builder = StateGraph(InterviewState)
interview_builder.add_node("generate_question", generate_question)
interview_builder.add_node("search_web", search_web)
interview_builder.add_node("search_wikipedia", search_wikipedia)
interview_builder.add_node("generate_answer", generate_answer)
interview_builder.add_node("save_interview", save_interview)
interview_builder.add_node("write_section", write_section)

# Flow
interview_builder.add_edge(START, "generate_question")
interview_builder.add_edge("generate_question", "search_web")
interview_builder.add_edge("generate_question", "search_wikipedia")
interview_builder.add_edge("search_web", "generate_answer")
interview_builder.add_edge("search_wikipedia", "generate_answer")
interview_builder.add_conditional_edges("generate_answer", route_messages,['generate_question','save_interview'])
interview_builder.add_edge("save_interview", "write_section")
interview_builder.add_edge("write_section", END)

interview_graph = interview_builder.compile()