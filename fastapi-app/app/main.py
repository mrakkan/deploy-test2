from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def root():
    return {"message": "ok", "port": os.getenv("PORT", "80")}

@app.get("/health")
def health():
    return {"status": "healthy"}