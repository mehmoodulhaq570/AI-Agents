# The finance agent which use the tool to give analyst recommendations

from phi.agent import Agent
from phi.model.groq import Groq
from phi.model.openai import OpenAIChat
from phi.model.google import Google
from phi.tools.yfinance import YFinanceTools
from dotenv import load_dotenv

load_dotenv()

agent = Agent (
    #model=Groq(id="llama-3.3-70b-versatile"),
    model=OpenAIChat(id="gpt-4o"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True)],
    show_tools_calls=True,
    markdown=True,
    instructions=['Use table to display data.'],
    #debug_mode=True
)

agent.print_response("Summarize and compare the analyst recommendation and fundamentals for Tesla and Nvidia")