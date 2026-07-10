#IMport libraries
from fastapi import FastAPI # used to create the backend API
from fastapi.middleware.cors import CORSMiddleware  # controls wether the frontend is allowed to call the backend
from db import fetch_schema, run_query
from claude_client import generate_sql
from pydantic import BaseModel  # this is used to define the shape of the request data

# frontend is on port 5173 whereas the backend is on 8000. Two different ports hence two different origins. CORS allows these two ports to talk to each other

# App setup (This is what Uvicorn runs)
app = FastAPI()

# 
origins = ["*"]     # any origin is allowed
    # "http://localhost",
    # "http://localhost:3000",
    # "http://localhost:5177",
    # "http://localhost:8000",
    #]

# this adds middleware.
# code that runs between responses and requests
app.add_middleware(
    CORSMiddleware, # what middleware that is being added
    allow_origins = origins, #what origins are allowed
    allow_credentials = False, #cookies -- dont need this 
    allow_methods = ["*"], # GET, POST, PUT, DELETE
    allow_headers = ["*"], # content-type
)


# @app.get("/")
# async def root():
#     return {"message": "Hello World"}

# defining the shape of the request
#describes what will be sent from the frontend
class QueryRequest(BaseModel):
    question: str   # must be a string


@app.post("/query") # creating a POST endpoint.

# The function that will be called after recieving the post request 
async def query(request: QueryRequest):
    sql = generate_sql(request.question, fetch_schema())
    result = run_query(sql)
    return result





