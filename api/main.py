from fastapi import FastAPI, Form, UploadFile, File
import logging
from api.helpers import get_answer

app = FastAPI()

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.get("/")
async def root():
    return {"message": "Welcome to TDS Solver API!"}

@app.post("/api/")
async def handle_question(
    question: str = Form(),  
    file: UploadFile | None = File(None)  # Optional file
):
    """
    Handles API requests by processing the question.
    The file is only for formality and is not processed.
    """
    if file:
        file_content = await file.read()
        file_name = file.filename
        logger.info(f"Received file: {file_name} ({len(file_content)} bytes)")

    answer = get_answer(question)  
    return {"answer": answer}