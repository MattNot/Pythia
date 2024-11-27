import ast
import astor
from typing import Annotated, Literal, TypedDict
from langgraph.graph.message import add_messages
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_openai import ChatOpenAI
from langchain_openai import OpenAI
from langchain_core.tools import tool
from langgraph.checkpoint.memory import MemorySaver
from langgraph.graph import END, START, StateGraph, MessagesState
from langgraph.prebuilt import ToolNode
from langchain_core.runnables import RunnableConfig


class PythonDocstringState(TypedDict):
    node: ast.FunctionDef
    comment: ast.Constant
    messages: Annotated[list, add_messages]

    def __init__(self, node: ast.FunctionDef):
        self.node = node


@tool
def generate_docstring(code: str):
    """Generates a docstring for a given Python code snippet."""
    llm = OpenAI()
    res = llm.invoke(input=
        'Write a docstring for the following function, DO NOT include ticks: ' + code).replace('"', "").replace("\n", "", 2)
    return res


class PythonDocstringGenerator:
    workflow: StateGraph
    node = ast.FunctionDef

    def insert_docstring(self, state: PythonDocstringState):
       return {'comment': ast.Constant("\n"+(' ' * (state['node'].col_offset+4)) + state['messages'][-1].content + '\n')}

    def start_node(self, state: PythonDocstringState):
        llm = ChatOpenAI()
        llm = llm.bind_tools([generate_docstring])
        return {'messages': [llm.invoke(state['messages'])]}

    def __init__(self, node: ast.FunctionDef):
        self.node = node
        self.workflow = StateGraph(PythonDocstringState)
        self.workflow.add_node('tools', ToolNode([generate_docstring]))
        self.workflow.add_node('start_node', self.start_node)
        self.workflow.add_node('insert_docstring', self.insert_docstring)
        self.workflow.add_edge(START, 'start_node')
        self.workflow.add_edge('start_node', 'tools')
        self.workflow.add_edge('tools', 'insert_docstring')
        self.workflow.add_edge('insert_docstring', END)
        self.graph = self.workflow.compile()

    def run(self):
        result = self.graph.invoke({'node': self.node, 'messages': [
            'Write a docstring for the following function, DO NOT include ticks: '
             + astor.to_source(self.node)]})
        return result