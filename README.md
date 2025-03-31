# TDS Solver API
This API provides answers to IIT Madras' Online Degree in Data Science graded assignments.

## How to Use
Send a `POST` request to `/api/` with a question (and an optional file).

## Example Request
```bash
curl -X POST "https://your-app.vercel.app/api/" \
  -H "Content-Type: multipart/form-data" \
  -F "question=Example Question 1"
