from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json()["status"] == "ok"

def test_predict():
    r = client.post("/predict", json={"x":[0,1,2]})
    assert r.status_code == 200
    assert r.json()["output"] == [1.0, 4.0, 7.0]
