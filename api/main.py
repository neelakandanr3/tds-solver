from fastapi import FastAPI, Form, File, UploadFile
from helpers import get_answer

app = FastAPI()

@app.post("/api/")
async def handle_question(
    question: str = Form(...),
    file: UploadFile | None = File(None)  # Accept file, but don't process it
):
    return {"answer": get_answer(question)}