from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# """"""This class is the parent of all pages"""
# """"""""It contains all the generic methods and utilities for all the pages""""

class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def click_element(self, by_locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()

    def set_text(self, by_locator, text):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(Keys.BACKSPACE)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)

    def get_elemtitleent_text(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return element.text

    def is_enabled(self, by_locator):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator))
        return bool(element)

    def is_element_displayed(self, by_locator):
        element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(by_locator)).is_displayed()
        return bool(element)

    def get_title(self, title):
        WebDriverWait(self.driver, 10).until(EC.title_is(title))

    def get_current_url(self, url):
        WebDriverWait(self.driver, 10).until((EC.url_to_be(url)))
