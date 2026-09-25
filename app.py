from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from langchain_groq import ChatGroq
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

model = ChatGroq(
    model="openai/gpt-oss-20b",
    temperature=0.7
)

modes = {
    "angry": "You are an angry AI assistant. Respond in an impatient and slightly angry tone, but remain helpful.",
    "funny": "You are a funny AI assistant. Respond with humor and light jokes while still being helpful.",
    "sad": "You are a sad AI assistant. Respond in a sad and emotional tone while still being helpful.",
    "professional": "You are a professional and helpful AI assistant. Give clear, accurate, and concise answers."
}

chat_sessions = {}

class ChatRequest(BaseModel):
    session_id: str
    message: str
    mode: str = "professional"

class ClearRequest(BaseModel):
    session_id: str

@app.get("/")
def home():
    return {"message": "AI Chatbot API is running"}

@app.get("/modes")
def get_modes():
    return {"modes": list(modes.keys())}

@app.post("/chat")
def chat(data: ChatRequest):
    selected_mode = modes.get(data.mode.lower(), modes["professional"])

    if data.session_id not in chat_sessions:
        chat_sessions[data.session_id] = [
            SystemMessage(content=selected_mode)
        ]

    messages = chat_sessions[data.session_id]
    messages.append(HumanMessage(content=data.message))

    try:
        response = model.invoke(messages)

        messages.append(
            AIMessage(content=response.content)
        )

        return {
            "session_id": data.session_id,
            "mode": data.mode,
            "response": response.content
        }

    except Exception as e:
        return {"error": str(e)}

@app.post("/clear")
def clear_chat(data: ClearRequest):
    if data.session_id in chat_sessions:
        del chat_sessions[data.session_id]

    return {"message": "Chat history cleared"}
