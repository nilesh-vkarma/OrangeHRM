from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class CommonStuff:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def click(self, path):
        try:
            element = self.wait.until(EC.element_to_be_clickable(path))
            element.click()
        except (TimeoutException, NoSuchElementException) as e:
            print(f"Error clicking element; Exception: {e}")

    def enter_text(self, by, value, text):
        try:
            element = self.wait.until(EC.visibility_of_element_located((by, value)))
            element.clear()
            element.send_keys(text)
        except (TimeoutException, NoSuchElementException) as e:
            print(f"Error entering text in element: {value}. Exception: {e}")

    def wait_for_element(self, value):
        try:
            self.wait.until(EC.visibility_of_element_located(value))
        except TimeoutException:
            print(f"Element not found: {value}")

    def is_element_present(self, value):
        try:
            self.driver.find_element(value)
            return True
        except NoSuchElementException:
            return False

    def get_element_text(self, by, value):
        try:
            element = self.wait.until(EC.visibility_of_element_located((by, value)))
            return element.text
        except (TimeoutException, NoSuchElementException) as e:
            print(f"Error getting text from element: {value}. Exception: {e}")
            return None
