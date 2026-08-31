import vertexai
from vertexai.generative_models import GenerativeModel
from google.oauth2 import service_account
import os
from dotenv import load_dotenv
load_dotenv()
print("PROJECT_ID:", os.getenv("PROJECT_ID"))
print("MODEL:", os.getenv("MODEL"))
print("LOCATION:", os.getenv("LOCATION"))
print("CREDENTIALS:", os.getenv("GOOGLE_APPLICATION_CREDENTIALS"))

# FIX 1 — use correct env variable names
project_id = os.getenv("PROJECT_ID")
location = os.getenv("LOCATION")

# FIX 2 — load credentials properly
creds = service_account.Credentials.from_service_account_file(
    os.getenv("GOOGLE_APPLICATION_CREDENTIALS")
)

# FIX 3 — pass credentials object, not string
vertexai.init(
    project=project_id,
    location=location,
    credentials=creds
)

# FIX 4 — test the model
model = GenerativeModel("gemini-2.5-flash")
print(model.generate_content("hello").text)