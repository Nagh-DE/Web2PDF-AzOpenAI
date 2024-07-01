from settings import set_llm_config
from tools.guidelines import guidelines_engine
from tools.webreader import web_reader_engine
from tools.report_generator import report_generator
from llama_index.core.agent import ReActAgent

from dotenv import load_dotenv

load_dotenv()
chat_llm, embed_llm = set_llm_config()


agent = ReActAgent.from_tools(
    tools=[
        guidelines_engine,
        web_reader_engine,
        report_generator
    ],
    llm=chat_llm,
    verbose=True
)

while True:
    user_input = input("You: ")
    if user_input.lower() == "quit":
        break
    response = agent.chat(user_input)
    print("Agent: ", response)
