from selenium.webdriver.common.by import By

from Pages.BasePage import BasePage
from config.config import TestData


class LoginPage(BasePage):
    Email = (By.ID, "login_field")
    Password = (By.ID, "password")
    Login_Button = (By.XPATH, "//input[@value='Sign in']")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)

    def get_login_page_title(self, title):
        return self.get_title(title)

    def do_login(self, username, password):
        self.set_text(self.Email, username)
        self.set_text(self.Password, password)
        self.click_element(self.Login_Button)
