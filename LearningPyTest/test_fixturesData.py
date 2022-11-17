import pytest


@pytest.mark.usefixtures("data_Load")
class TestExample2:

    def test_editProfile(self, data_Load):
        print(data_Load)
        print("======================")
        print(data_Load[0])
        print(data_Load[1])
        print(data_Load[2])
        print(data_Load[3])

