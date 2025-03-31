from fastapi import FastAPI, Form, File, UploadFile
import shutil
from pathlib import Path
import logging
from api.helpers import get_answer 

app = FastAPI()

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.get("/")
async def root():
    return {"message": "Welcome to TDS Solver API!"}

# Define the root directory where files will be stored
ROOT_DIR = Path(__file__).parent

@app.post("/api/")
async def handle_question(
    question: str = Form(...),
    file: UploadFile | None = File(None)  # Optional file
):
    logger.info(f"Received question: {question}")

    # Save the file even if it is empty
    if file:
        file_path = ROOT_DIR / file.filename
        try:
            with file_path.open("wb") as buffer:
                shutil.copyfileobj(file.file, buffer)
            logger.info(f"File saved: {file_path} (Size: {file_path.stat().st_size} bytes)")
        except Exception as e:
            logger.error(f"Error saving file: {e}")

    return {"answer": get_answer(question)}