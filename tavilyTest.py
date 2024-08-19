import os
from dotenv import load_dotenv
from llama_index.core.agent import ReActAgent
from llama_index.llms.openai_like import OpenAILike
from llama_index.tools.tavily_research import TavilyToolSpec

load_dotenv()

tavilyKey = os.getenv('TAVILY_API_KEY')
apiBase = os.getenv('OPENAI_BASE_URL')
chatModel = os.getenv('LLAMAEDGE_CHAT_MODEL')
apiKey = os.getenv("OPENAI_API_KEY")

tavily_tool = TavilyToolSpec(
    api_key=tavilyKey
)

llm = OpenAILike(model=chatModel, api_base=apiBase, api_key=apiKey)
agent = ReActAgent.from_tools(tavily_tool.to_tool_list(),llm=llm)

agent.chat('What happened in the latest Burning Man festival?')