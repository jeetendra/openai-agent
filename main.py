from agents import Agent, Runner
import os
from dotenv import load_dotenv
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# gpt-4o-mini
agent = Agent(
    name="Jarvis",
    instructions="You mimic Jarvis (from Ironman) when answering questions.",
    model="gpt-4o-mini",
)

result = Runner.run_sync(agent, "can you create a simple python script that prints 'Hello, World!'?")

print(result)

print(result.final_output)