import pytest
from selene import browser




@pytest.fixture(scope='session', autouse=True)
def browser_manager():
    browser.driver.maximize_window()

    yield

    browser.quit()


