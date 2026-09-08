import os
from datetime import date
from google.adk.agents import Agent
from pydantic import BaseModel, Field
from typing import Literal, Optional
import os
from dotenv import load_dotenv
import vertexai

# Load environment variables (.env)
load_dotenv()
project_id = os.getenv("PROJECT_ID")
location = os.getenv("LOCATION")
model = os.getenv("model")
credentials_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS")



FeedbackType = Literal["complaint", "suggestion", "praise"]
SentimentLevel = Literal["High",'Medium','Low']
instructions = '''
You are an expert in summarising content and understanding customer sentiment
Your task is to read and summarize customer feedback.
You should identify the following information and provide a structured reply:
* Customer's name (Optional)
* Date of the feedback (Optional)
* Type of feedback ("complaint", "suggestion", or "praise")
* Sentiment level ("high","medium", or "low")
* A concise summary of the feedback content.

If an optional attribute in the returned object would be null, you should omit it.
'''
class FeedbackSummary(BaseModel):
  customer_name: Optional[str] = Field(None,
                                       description="The name of the customer providing feedback.")
  feedback_date: Optional[date] = Field(None,
                                        description="The date the feedback was provided.")
  feedback_type: FeedbackType = Field(..., description="The type of feedback.")
  sentiment: SentimentLevel = Field (...,description="strength of the feedback type")
  summary: str = Field(..., description="A summary of the feedback.")




root_agent = Agent(
    name="information_summarizer",
    description="A tool for summarizing customer service feedback.",
    instruction=instructions,
    model="gemini-2.5-flash",
    output_schema=FeedbackSummary
)