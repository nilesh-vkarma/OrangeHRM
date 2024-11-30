import pytest
from selenium import webdriver
from configReader import ConfigReader
from Stuff.Pages.LogIn_page import Login


@pytest.fixture(scope="class")
def initial_setup():
    # Init browser
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.delete_all_cookies()

    # Instance of Config reader
    config = ConfigReader()

    # Initialize the driver
    driver.get(config.get_value("default", "url"))

    # Whatever written after yield keyword will be same as tearDown, run after all test
    yield
    driver.quit()


@pytest.mark.usefixtures("initial_setup")
class TestLogin:

    def test_login(self):
        driver.implicitly_wait(10)
        page = Login(driver)  # Instance of Login page file.

        page.enter_username()  # This is how we can use methods of Login file.
        page.enter_password()
        page.click_login_button()

        # Add assertions to verify login success
        assert "OrangeHRM" in driver.title  # Adjust based on your app's behavior
