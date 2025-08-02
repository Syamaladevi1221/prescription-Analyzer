from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from utils.ocr import extract_text_from_image
from utils.parser import analyze_prescription_text
import io

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class TextInput(BaseModel):
    text: str

@app.post("/extract_text")
async def extract_text(file: UploadFile = File(...)):
    contents = await file.read()
    text = extract_text_from_image(contents)
    return {"text": text}

@app.post("/analyze_prescription")
async def analyze_prescription(input: TextInput):
    return analyze_prescription_text(input.text)
