def login(username: str, password: str) -> bool:
    """Simple Login Function for testing."""
    if username == "munky" and password =="password123":
        return True
    return False

if __name__ == "__main__":
    print("Login attempt 1:", login("munky", "password123"))
    print("Login attempt 2:", login("wrong", "guess"))
