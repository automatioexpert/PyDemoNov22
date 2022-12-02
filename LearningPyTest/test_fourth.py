import pytest


@pytest.mark.usefixtures("setUp") # Automatically applied to all the methods of the class
class TestExample:

    def test_4th1(self):
        print("4th test executing")


    def test_4th2(self):
        print("4th test executing")

    def test_4th3(self):
        print("4th test executing")

    def test_4th4(self):
        print("4th test executing")