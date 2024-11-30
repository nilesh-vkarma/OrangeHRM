from Stuff.Pages.CommonStuff import CommonStuff
from selenium.webdriver.common.by import By
from configReader import ConfigReader


class Login:
    login_Button = (By.XPATH, '//*[@type = "submit"]')

    # __init__ method is called as constructor, that will be auto call whenever the instance of the class will be created
    # We can create instance of pages in init if the same instance will gonna use in upcoming max methods
    def __init__(self, driver):
        self.driver = driver
        self.fromSecretFile = ConfigReader()  # We gonna use the configReader in many  upcoming methods, so we declared it here.
        self.do = CommonStuff(self.driver)

    def enter_username(self):
        username = self.fromSecretFile.get_value("default", "username")
        self.do.enter_text(By.NAME, "username", username)

    def enter_password(self):
        password = self.fromSecretFile.get_value("default", "password")
        self.do.enter_text(By.NAME, "password", password)

    def click_login_button(self):
        self.do.click(self.login_Button)
