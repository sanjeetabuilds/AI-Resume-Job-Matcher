from fastapi import FastAPI

app = FastAPI(
    title="AI Resume & Job Matching Platform",
    description="Backend API for resume processing and intelligent job matching",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "AI Resume & Job Matching API is running!"
    }


@app.get("/health")
def health_check():
    return {
        "status": "healthy"
    }