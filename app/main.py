from fastapi import FastAPI

app = FastAPI(
    title="DevSecOps Lab API",
    version="1.0.0"
)

# HEALTHCHECK (obligatoire en production)
@app.get("/health")
def health():
    return {
        "status": "UP",
        "service": "devsecops-api"
    }

# ROOT
@app.get("/")
def root():
    return {
        "message": "DevSecOps API running"
    }

# FAKE DATABASE (simple pour demo)
TASKS = []

@app.post("/tasks")
def create_task(task: str):
    TASKS.append(task)
    return {
        "status": "created",
        "task": task
    }

@app.get("/tasks")
def get_tasks():
    return {
        "count": len(TASKS),
        "tasks": TASKS
    }