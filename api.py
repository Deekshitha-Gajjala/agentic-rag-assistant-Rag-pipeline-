from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List

from agent import run_agent
from tools.pdf_tool import extract_pdf_text
from tools.speech_to_text import transcribe_audio


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Store uploaded PDF text
pdf_text = ""


class Query(BaseModel):
    question: str
    history: list = []


@app.get("/")
def home():
    return {
        "message": "Agentic RAG Assistant API Running"
    }


@app.post("/chat")
def chat(query: Query):

    global pdf_text

    prompt = f"""
PDF Content:

{pdf_text}

Question:
{query.question}
"""

    answer = run_agent(
        prompt,
        query.history
    )

    return {
        "answer": answer
    }


@app.post("/upload-pdf")
async def upload_pdf(file: UploadFile = File(...)):

    global pdf_text

    pdf_text = extract_pdf_text(file.file)

    print("\n========== PDF UPLOADED ==========")
    print(pdf_text[:1500])
    print("==================================\n")

    return {
        "message": "PDF uploaded successfully",
        "characters": len(pdf_text)
    }


@app.post("/voice-chat")
async def voice_chat(file: UploadFile = File(...)):

    global pdf_text

    audio_path = file.filename

    with open(audio_path, "wb") as buffer:
        buffer.write(await file.read())

    question = transcribe_audio(audio_path)

    prompt = f"""
PDF Content:

{pdf_text}

Question:
{question}
"""

    answer = run_agent(
        prompt,
        []
    )

    return {
        "question": question,
        "answer": answer
    }