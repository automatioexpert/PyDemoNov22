import pytest


@pytest.fixture(scope="class")
def setUp():
    print("Setup -- I will be executed first..Common fixture is called")
    yield
    print("I will be executed last in the test execution")


@pytest.fixture()
def data_Load():
    print("User profile data is being created")
    return ["Steve","Hill","hill343399@gmail.com","Ghurha Baliyari"]

@pytest.fixture(params=["chrome","Firefox","IE","Safari","Edge","Chromium"])
def crossBrowser(request):
    return request.param


