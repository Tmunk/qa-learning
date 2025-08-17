#tests/test_sample.py

def test_login(sample_data):
    assert sample_data["username"] == "munky"


# """ def test_numbers():
#     assert 2 + 2 == 4

# def test_strings():
#     assert "hello".upper() == "HELLO" """