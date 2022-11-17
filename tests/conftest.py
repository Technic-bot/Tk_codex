import pytest
from backend.codex import app

@pytest.fixture
def client():
    return app.test_client()
