from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import openai
#from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize FastAPI app
app = FastAPI()

# Replace with provided API key
openai.api_key_path = os.getenv("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")

# Define request model
class UserQuery(BaseModel):
    query : str
    
# Helper function to interact with OpenAI API
def get_openai_response(user_query: str) -> str:
    try: 
        response = openai.Completion.create(
            engine="gpt-3.5-turbo",  
            messages=[
                {"role": "system", "content": (
                    "You are an AI assistant specializing in answering general and healthcare-related questions. "
                    "If a user asks a programming or mathematical question, respond with: "
                    "'Sorry, I cannot answer this query, please do not ask queries related to programming or mathematics.'"
                )},
                {"role": "user", "content": user_query}
            ],
            max_tokens=100,
            temperature=0.7
            )
        return response['choices'][0]['message']['content'].strip()
    except Exception as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail="Error processing request")

# Define the API endpoint
@app.post("/user-query")
async def user_query(user_query: UserQuery):
    response_text = get_openai_response(user_query.query)
    return {"response": response_text}


