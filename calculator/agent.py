# agent.py
import os
from dotenv import load_dotenv
from google.oauth2 import service_account
import vertexai
from google.adk.agents import Agent

# Load environment variables (.env)
load_dotenv()

project_id = os.getenv("PROJECT_ID")
location = os.getenv("LOCATION")
credentials_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")

if credentials_path:
    creds = service_account.Credentials.from_service_account_file(credentials_path)
    vertexai.init(
        project=project_id,
        location=location,
        credentials=creds
    )

def summation(numbers: list[float]) -> float:
    """Sums a list of numbers."""
    return sum(numbers)
def division(x:float,y:float) -> float:
    """Divide x by y"""
    return x/y
def substract(x:float,y:float)->float:
    """Substracts y from x"""
    return x-y
def multiply(x:float,y:float)->float:
    """multiply x and y"""
    return x*y

# The console runner looks for this Agent instance
root_agent = Agent(
    name="calculator_tools",
    description="Multiple tools to do different mathematical calculations",
    model="gemini-2.5-flash",
    tools=[summation,division,substract,multiply],
    instruction="You are a calculator and calculate arithmetic."
)