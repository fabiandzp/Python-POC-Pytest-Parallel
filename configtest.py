import pytest
from selenium import webdriver


@pytest.fixture(scope="session")
def setup(request):
    print("Initiating Chrome Driver")
    driver = webdriver.Chrome()
    session = request.node
    for item in session.items:
        cls = item.getparent(pytest.Class)
        setattr(cls.obj, "driver", driver)
    driver.get("https://www.google.com")
    driver.maximize_window()

    yield driver
    driver.close()