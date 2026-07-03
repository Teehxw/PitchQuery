from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from db import fetch_schema, run_query
from claude_client import generate_sql
from pydantic import BaseModel



app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
    "http://localhost:5173",
    "http://localhost:8000",
    ]

app.add_middleware(
    CORSMiddleware, 
    allow_origins = origins, 
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)
@app.get("/")
async def root():
    return {"message": "Hello World"}

class QueryRequest(BaseModel):
    question: str

@app.post("/query")
async def query(request: QueryRequest):
    sql = generate_sql(request.question, fetch_schema())
    result = run_query(sql)
    return result





