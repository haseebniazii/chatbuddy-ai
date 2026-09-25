# 🤖 ChatBuddy AI

<p align="center">
  <b>An AI-powered conversational chatbot with multiple personality modes, session-based chat history, and a modern interactive interface.</b>
</p>

<p align="center">
  🚀 AI Chatbot &nbsp; | &nbsp; 🧠 Conversational AI &nbsp; | &nbsp; 💬 Multi-Mode Chat &nbsp; | &nbsp; ⚡ FastAPI
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python">
  <img src="https://img.shields.io/badge/FastAPI-Backend-009688?style=for-the-badge&logo=fastapi">
  <img src="https://img.shields.io/badge/LangChain-AI-green?style=for-the-badge">
  <img src="https://img.shields.io/badge/Groq-LLM-orange?style=for-the-badge">
  <img src="https://img.shields.io/badge/Vercel-Deployed-black?style=for-the-badge&logo=vercel">
</p>

---

## 🌐 Live Demo

<p align="center">
  <a href="https://chatbuddy-ai-seven.vercel.app/">
    <img src="https://img.shields.io/badge/🚀_Try_ChatBuddy_AI-Live_Demo-brightgreen?style=for-the-badge">
  </a>
</p>

👉 **Live Application:**
https://chatbuddy-ai-seven.vercel.app/

---

## 📌 About The Project

**ChatBuddy AI** is an AI-powered conversational chatbot designed to provide interactive, context-aware, and personality-driven conversations.

Instead of providing responses in only one style, ChatBuddy allows users to choose between multiple AI personality modes.

The application combines a modern web interface with an AI-powered Python backend to create a complete chatbot experience.

ChatBuddy maintains conversation history for each session, allowing the AI to understand previous messages and provide more contextual responses.

---

## ✨ Features

* 🤖 AI-powered conversations
* 🧠 Context-aware responses
* 💬 Interactive chat interface
* 👤 Session-based conversation history
* 🎭 Multiple AI personality modes
* 💼 Professional responses
* 😂 Funny responses
* 😠 Angry-style responses
* 😢 Sad/emotional responses
* 🗑️ Clear conversation functionality
* ⚡ Fast API-based communication
* 🌐 Responsive web interface
* 🔐 Secure API key management
* ☁️ Cloud deployment
* 📱 Mobile-friendly design

---

## 🎭 AI Personality Modes

ChatBuddy AI includes four different conversation modes.

| Mode                | Description                                                          |
| ------------------- | -------------------------------------------------------------------- |
| 💼 **Professional** | Provides clear, concise, accurate, and professional responses        |
| 😂 **Funny**        | Adds humor and light jokes while remaining helpful                   |
| 😠 **Angry**        | Responds in an impatient and slightly angry tone while still helping |
| 😢 **Sad**          | Responds with a sad and emotional tone while remaining helpful       |

Users can select a mode according to the type of conversation they want.

---

## 🧠 AI Model

ChatBuddy AI uses:

```text
openai/gpt-oss-20b
```

The model receives the conversation history along with the selected personality instructions and generates an appropriate response.

---

## ⚙️ How It Works

```text
User
  ↓
ChatBuddy Web Interface
  ↓
User Message + Selected Mode
  ↓
FastAPI Backend
  ↓
Session History
  ↓
LangChain
  ↓
Groq AI Model
  ↓
Generated Response
  ↓
ChatBuddy Interface
```

---

## 🛠️ Technologies Used

### Backend

* 🐍 Python
* ⚡ FastAPI
* 🧠 LangChain
* 🚀 Groq
* 📦 Pydantic
* 🔐 Python Dotenv

### Frontend

* 🌐 HTML5
* 🎨 CSS3
* ⚙️ JavaScript
* 📱 Responsive Design

### Deployment

* ☁️ Vercel
* 🐙 GitHub

---

## 📁 Project Structure

```text
chatbuddy-ai/
│
├── app.py
├── index.html
├── requirements.txt
├── .gitignore
├── README.md
└── LICENSE
```

Sensitive environment variables such as API keys are intentionally excluded from the repository.

---

## 🔌 API Endpoints

### 🏠 API Status

```http
GET /
```

Used to verify that the API is running.

Example response:

```json
{
  "message": "AI Chatbot API is running"
}
```

---

### 🎭 Get Chat Modes

```http
GET /modes
```

Returns the available AI personality modes.

Example:

```json
{
  "modes": [
    "angry",
    "funny",
    "sad",
    "professional"
  ]
}
```

---

### 💬 Send Message

```http
POST /chat
```

Example request:

```json
{
  "session_id": "user123",
  "message": "Explain machine learning.",
  "mode": "professional"
}
```

Example response:

```json
{
  "session_id": "user123",
  "mode": "professional",
  "response": "Machine learning is a branch of artificial intelligence..."
}
```

---

### 🗑️ Clear Conversation

```http
POST /clear
```

Example request:

```json
{
  "session_id": "user123"
}
```

Example response:

```json
{
  "message": "Chat history cleared"
}
```

---

## 🔐 Environment Variables

The project requires a Groq API key.

Create a `.env` file in the project directory:

```env
GROQ_API_KEY=your_groq_api_key_here
```

> ⚠️ Never expose or commit your API key to GitHub.

The `.env` file should remain excluded through `.gitignore`.

---

## ⚙️ Local Installation

### 1. Clone Repository

```bash
git clone https://github.com/haseebniazii/chatbuddy-ai.git
```

### 2. Open Project Directory

```bash
cd chatbuddy-ai
```

### 3. Create Virtual Environment

```bash
python -m venv .venv
```

### 4. Activate Virtual Environment

#### Windows

```bash
.venv\Scripts\activate
```

#### Linux / macOS

```bash
source .venv/bin/activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

### 6. Add Environment Variable

Create:

```text
.env
```

and add:

```env
GROQ_API_KEY=your_groq_api_key_here
```

### 7. Start The Application

```bash
uvicorn app:app --reload
```

The local API should then be available at:

```text
http://127.0.0.1:8000
```

FastAPI interactive documentation:

```text
http://127.0.0.1:8000/docs
```

---

## 💬 Session-Based Chat History

Each user receives a unique session ID.

ChatBuddy stores messages associated with that session so previous messages can be passed back to the AI model.

The conversation follows:

```text
System Message
      ↓
User Message
      ↓
AI Response
      ↓
Next User Message
      ↓
Previous Context + New Message
      ↓
Next AI Response
```

This allows ChatBuddy to maintain conversational context during the active session.

---

## 🔒 Security

Sensitive information is kept outside the public repository.

The following files and directories are excluded using `.gitignore`:

```text
.env
.venv/
venv/
__pycache__/
```

API keys should always be configured through environment variables when deploying the application.

---

## 💡 What I Learned

Through this project, I practiced:

* Building AI-powered applications
* Working with Large Language Models
* Integrating LangChain with an LLM provider
* Developing APIs with FastAPI
* Using Pydantic models
* Managing conversation history
* Building session-based chatbot systems
* Prompt engineering
* Creating multiple AI personalities
* Connecting frontend and backend
* Working with REST API endpoints
* Handling CORS
* Managing environment variables securely
* Deploying an AI web application

---

## 🚀 Future Improvements

Future versions of ChatBuddy AI can include:

* 🔐 User authentication
* 💾 Database-based persistent chat history
* 📝 Multiple saved conversations
* 🎙️ Voice input
* 🔊 Text-to-speech responses
* 📎 File uploads
* 🖼️ Image understanding
* 🔍 Web search integration
* 📚 Document-based question answering
* 🌙 Dark/light theme switching
* ⚡ Streaming AI responses
* 🧠 Additional AI models
* 🎭 More personality modes

---

## 🔗 Links

**🚀 Live Demo**

https://chatbuddy-ai-seven.vercel.app/

**💻 GitHub Repository**

https://github.com/haseebniazii/chatbuddy-ai

---

## 👨‍💻 Author

### Haseeb Khan

Computer Science student focused on **Python, Machine Learning, Artificial Intelligence, and practical AI applications**.

GitHub: **@haseebniazii**

---

<p align="center">
  ⭐ If you found ChatBuddy AI useful, consider giving the repository a star!
</p>

<p align="center">
  Made with ❤️ using Python & AI
</p>

---

## 📜 License

This project is licensed under the **MIT License**.
