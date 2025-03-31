from fastapi import FastAPI, Form, UploadFile, File
import logging
from api.helpers import get_answer  # Import the helper function

app = FastAPI()

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.get("/")
async def root():
    return {"message": "Welcome to TDS Solver API!"}

@app.post("/api/")
async def handle_question(
    question: str = Form(...),  
    file: UploadFile | None = File(None)  # File is optional and not processed
):
    """
    Handles API requests by processing the question and ignoring the file.
    """
    # Log file details for debugging (if a file is sent)
    if file:
        logger.info(f"Received file: {file.filename} (Not processed)")

    # Get predefined answer from helpers.py
    answer = get_answer(question)
    return {"answer": answer}