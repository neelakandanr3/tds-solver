from fastapi import FastAPI, Form, File, UploadFile
from api.helpers import get_answer

app = FastAPI()

@app.post("/api/")
async def solve_question(question: str = Form(...), file: UploadFile = File(None)):
    # Placeholder response – modify this to return actual answers
    return {"answer": "1234567890"}
