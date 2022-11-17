import pytest

"""
You can mark test with @pytest.mark.smoke and then run with -m
"""
def test_1():
    print("Running first")


def test_2():
    print("Running second")


@pytest.mark.xfail
def test_3():
    print("Running third")

@pytest.mark.skip
def test_four():
    msg="Hello"
    assert msg =="Hi","Test Failed because strings are not matching"

def test_5():
    a=1
    b=2
    assert a==2,"Addition do no match"

def test_prod1():
    print("Running prod1")

@pytest.mark.smoke
def test_prod2():
    print("Running prod2:marked as smoke test")

@pytest.mark.smoke
def test_prod3():
    print("Running prod3:marked as smoke test")

@pytest.fixture()
def setUp():
    print("Fixture: I will be executed first")

def test_fixtureDemo(setUp):
    print("I will execute steps in fixture demo method")













