from fastapi import FastAPI, Form, File, UploadFile
from api.helpers import get_answer

app = FastAPI()

@app.post("/api/")
async def answer_question(question: str = Form(...), file: UploadFile = None):
    answer = get_answer(question, file)
    return {"answer": answer}
