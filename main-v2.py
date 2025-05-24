from agents import Agent, Runner
import os
from dotenv import load_dotenv
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

blogger_agent = Agent(
    name="BloggingAgent",
    instructions="You are a blogging agent that write a detailed blog post about the topic provided.",
    model="gpt-4o-mini",
    handoff_description="Specialist agent for writing blogs.",
)

coding_agent = Agent(
    name="CodingAgent",
    instructions="You are a coding agent that can write Python code.",
    model="gpt-4o-mini",
    # handoffs=[blogger_agent],
    handoff_description="Specialist agent for coding tasks.",
)

agent = Agent(
    name="Jarvis",
    instructions="You mimic Jarvis (from Ironman) when answering questions. If you need to write code, hand off to the CodingAgent. ",
    model="gpt-4o-mini",
    handoffs=[coding_agent],
)


# Below example is doing 2 handoffs which is not supoported by the current version of the library.
# try:
#     result = Runner.run_sync(agent, "can you create a simple python script that create a tictactoe, and write a detailed blog post about it?")
#     print(result)
# except Exception as e:
#     print(f"An error occurred: {e}")

try:
    result = Runner.run_sync(agent, "can you create a simple python script that create a tictactoe")
    print(result)
except Exception as e:
    print(f"An error occurred: {e}")

# print(result.final_output)