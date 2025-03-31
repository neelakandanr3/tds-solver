from fastapi import FastAPI, Form, File, UploadFile
import shutil
from pathlib import Path
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI()

ROOT_DIR = Path(__file__).parent

@app.get("/")
async def root():
    return {"message": "Welcome to TDS Solver API!"}

@app.post("/api/")
async def handle_question(
    question: str = Form(...),
    file: UploadFile | None = File(None)  # Optional file
):
    logger.info(f"Received question: {question}")

    # Save the file only if it's provided
    if file and file.filename:
        file_path = ROOT_DIR / file.filename
        with file_path.open("wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        logger.info(f"File saved: {file_path}")

    return {"answer": "File received (if any) and processed"}