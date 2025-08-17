#tests/conftest.py

import pytest

@pytest.fixture
def sample_data():
    return {"username": "munky", "password": "12345"}

