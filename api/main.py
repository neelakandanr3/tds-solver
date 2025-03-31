from fastapi import FastAPI, Form, File, UploadFile
from fastapi.responses import JSONResponse, PlainTextResponse
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
    question: str = Form(...),
    file: UploadFile | None = File(None)  # Optional file
):
    answer = get_answer(question)

    # Ensure it's returned as a clean text response
    return PlainTextResponse(content=f'{{"answer": "{answer}"}}', media_type="application/json")