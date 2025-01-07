# This code is just to check the succesful working of Groq API key.

from phi.agent import Agent
from phi.model.groq import Groq
from dotenv import load_dotenv

load_dotenv()

agent = Agent (
    model=Groq(id="llama-3.3-70b-versatile")
)

agent.print_response("Write two sentence poem that show the affection of brids for each others")