from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def health():
    return {"status": "healthy"}
