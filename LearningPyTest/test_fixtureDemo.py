import pytest


@pytest.fixture()
def setUp():
    print("Fixture setup-I will be executed first")
    yield
    print("Yield...I will be executed last.")

def test_fixtureDemo(setUp):
    print("I will execute steps in fixture demo method")
