import os
import uvicorn
from fastapi import FastAPI
from app.routers import mp3

app  = FastAPI(
    title="Youtube to MP3 Converter",
    description="A simple API to convert YouTube videos to MP3.",
    version="1.0.0"
)

app.include_router(mp3.router)

@app.on_event("startup")
def setup_folders():
    """
    Setup folders or perform initialization tasks on app startup.
    """
    from app.core.utils import OUTPUT_DIR
    os.makedirs(OUTPUT_DIR, exist_ok=True)

if __name__ == "__main__":
    uvicorn.run("app.main:app", host="127.0.0.1", port=8000, reload=True)