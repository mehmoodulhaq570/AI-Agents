# This agent consist of team of agents which use the tool to perform mutiple actions at once

from phi.agent import Agent
from phi.model.groq import Groq
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.yfinance import YFinanceTools
from dotenv import load_dotenv

load_dotenv()

web_agent = Agent (
    name="Web Agent",
    model= Groq(id="llama-3.3-70b-versatile"),
    tools=[DuckDuckGo()],
    instructions=['Always include the source'],
    show_tools_call=True,
    markdown=True,
)

finance_agent = Agent (
    name = "Finance Agent",
    role = "Get financial data",
    model=Groq(id="llama-3.3-70b-versatile"),
    tools=[YFinanceTools(stock_price=True, analyst_recommendations=True, stock_fundamentals=True)],
    show_tools_calls=True,
    markdown=True,
    instructions=['Use table to display data.'],
)

agent_team = Agent(
    team = [web_agent, finance_agent],
    instructions=['Always include the source', 'Use table to display data.'],
    show_tools_calls=True,
    markdown=True,
)

agent_team.print_response("Summarize analyst recommendation and share the latest new for Nvidia", stream=True)