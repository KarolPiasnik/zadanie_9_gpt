import openai

from fastapi import FastAPI
from pydantic import BaseModel
from pydantic_settings import BaseSettings
from fastapi.middleware.cors import CORSMiddleware

class Settings(BaseSettings):
    OPENAI_API_KEY: str = 'YOUR_OPENAI_API_KEY'

    class Config:
        env_file = '.env'

settings = Settings()
openai.api_key = settings.OPENAI_API_KEY

class Prompt(BaseModel):
    text: str

app = FastAPI()

origins = [
    "http://localhost:5555"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/chat")
async def getChat():
    return {"response": "Hello World chat"}

@app.post("/chat")
async def postChat(prompt: Prompt):
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": prompt.text}])
    result = response.choices[0].message.content
    return {"answer": result}