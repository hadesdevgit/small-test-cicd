from fastapi.testclient import TestClient

from cicd_sample.api import app


def test_add_endpoint() -> None:
    client = TestClient(app)
    resp = client.get("/add", params={"a": 2, "b": 3})
    assert resp.status_code == 200
    assert resp.json() == {"result": 5}


def test_add_endpoint_invalid_input() -> None:
    client = TestClient(app)
    resp = client.get("/add", params={"a": "nope", "b": 3})
    assert resp.status_code == 422
