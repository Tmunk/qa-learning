#tests/unit/test_sample.py
from qa_learning.app import login
import pytest


def test_login(sample_data):
    assert sample_data["username"] == "munky"

@pytest.mark.parametrize("username,password,expected_result", [
    ("munky", "password123", True),
    ("wronguser", "password123", False),
    ("munky", "wrongpass", False),
])

def test_login_with_params(username, password, expected_result):
    login_success = login(username, password)
    assert login_success == expected_result
