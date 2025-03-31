from fastapi import FastAPI, Form, File
import logging
from api.helpers import get_answer  # Importing the answer function

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
    file: bytes | None = File(None)  # File is now treated as optional raw bytes
):
    """
    Handles API requests by processing the question and completely ignoring the file.
    """
    # Log that a file was received (for formality)
    if file is not None:
        logger.info("File received but ignored.")

    # Get predefined answer from helpers.py
    answer = get_answer(question)
    return {"answer": answer}