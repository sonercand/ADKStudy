# agent.py
import os
from dotenv import load_dotenv
from google.oauth2 import service_account
import vertexai
from google.adk.agents import Agent
from pydantic import BaseModel, Field
from typing import Literal, Optional
from .instructions import instruction
from .tools import set_home_location,add_city,create_itinerary
# Load environment variables (.env)
load_dotenv()
project_id = os.getenv("PROJECT_ID")
location = os.getenv("LOCATION")
credentials_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
model = os.getenv("MODEL")

instruction = ''''''
root_agent = Agent(
  name="travel_agent",
  description="An agent that can help plan a multi-step trip.",
  instruction=instruction,
  model=model,
  tools=[set_home_location, add_city, create_itinerary]
)