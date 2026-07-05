from langgraph.graph import StateGraph, START, END
from graph.schemas.state_ResearchGraphState import ResearchGraphState
from graph.analysts.create_analysts import create_analysts
from graph.humanFeedback.human_feedback import human_feedback
from graph.write import write_report
from graph.write import write_introduction
from graph.write import write_conclusion
from graph.write import finalize_report
from graph.Interviews.initiate_all_interviews import initiate_all_interviews
from graph.graphBuilder.interview_graph import interview_graph

# Add nodes and edges 
builder = StateGraph(ResearchGraphState)
builder.add_node("create_analysts", create_analysts)
builder.add_node("human_feedback", human_feedback)
builder.add_node("conduct_interview", interview_graph)
builder.add_node("write_report",write_report)
builder.add_node("write_introduction",write_introduction)
builder.add_node("write_conclusion",write_conclusion)
builder.add_node("finalize_report",finalize_report)

# Logic
builder.add_edge(START, "create_analysts")
builder.add_edge("create_analysts", "human_feedback")
builder.add_conditional_edges("human_feedback", initiate_all_interviews, ["create_analysts", "conduct_interview"])
builder.add_edge("conduct_interview", "write_report")
builder.add_edge("conduct_interview", "write_introduction")
builder.add_edge("conduct_interview", "write_conclusion")
builder.add_edge(["write_conclusion", "write_report", "write_introduction"], "finalize_report")
builder.add_edge("finalize_report", END)

# Compile
graph = builder.compile(interrupt_before=['human_feedback'])