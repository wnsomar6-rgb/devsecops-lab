from fastapi import FastAPI

app = FastAPI(
    title="DevSecOps Lab API",
    version="1.0.0"
)

# Route de santé (obligatoire en entreprise)
@app.get("/health")
def health_check():
    return {
        "status": "OK",
        "message": "API is running"
    }

# Route principale
@app.get("/")
def root():
    return {
        "message": "Welcome to DevSecOps Lab API"
    }

# Exemple de vraie API (mini feature métier)
tasks = []

@app.post("/tasks")
def create_task(task: str):
    tasks.append(task)
    return {
        "message": "Task created",
        "task": task
    }

@app.get("/tasks")
def get_tasks():
    return {
        "tasks": tasks
    }