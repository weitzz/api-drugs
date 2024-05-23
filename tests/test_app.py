from fastapi.testclient import TestClient

from api_drugs_fastapi.app import app

client = TestClient(app)
