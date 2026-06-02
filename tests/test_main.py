from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_root():
    r = client.get("/")
    assert r.status_code == 200
    assert "message" in r.json()

def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "UP"

def test_create_task():
    r = client.post("/tasks?task=test")
    assert r.status_code == 200
    assert r.json()["status"] == "created"

def test_get_tasks():
    r = client.get("/tasks")
    assert r.status_code == 200
    assert "tasks" in r.json()