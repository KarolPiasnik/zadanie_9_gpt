from fastapi import (
    FastAPI, Request, Response
)
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
import httpx
import asyncio



app = FastAPI()

# locate templates
templates = Jinja2Templates(directory="templates")

class Prompt(BaseModel):
    text: str

@app.get("/")
def get_home(request: Request):
    return templates.TemplateResponse("chat.html", {"request": request})

@app.websocket("/chat")
async def get_user(prompt: Prompt):
    return httpx.post('http://localhost:8000', data={'text': prompt.text})



