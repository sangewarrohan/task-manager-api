from fastapi import FastAPI

app = FastAPI(
    title="Task Manager API",
    version="1.0.0",
    description="Backend API for managing tasks."
)


@app.get("/")
def root():
    return {
        "message": "Task Manager API is running 🚀"
    }