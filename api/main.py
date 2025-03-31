from fastapi import FastAPI, Form, File, UploadFile
from fastapi.responses import JSONResponse
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
    
    # Ensure clean JSON output
    return JSONResponse(content={"answer": answer})