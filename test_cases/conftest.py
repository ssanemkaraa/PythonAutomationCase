import pytest


@pytest.fixture(autouse=True)
def run_around_tests():
    print("\nTest started\n")
    yield
    print("\nTest finished\n")