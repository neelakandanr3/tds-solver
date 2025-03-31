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

# Define the directory where files will be stored
ROOT_DIR = Path(__file__).parent

@app.post("/api/")
async def handle_question(
    question: str = Form(...),
    file: UploadFile | None = File(None)  # Optional file
):
    # If a file is uploaded, save it with the same filename and extension
    if file:
        file_path = ROOT_DIR / file.filename
        with file_path.open("wb") as buffer:
            shutil.copyfileobj(file.file, buffer)
        logger.info(f"File saved: {file_path}")

    return {"answer": get_answer(question)}