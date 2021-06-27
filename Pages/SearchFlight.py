import time

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from Pages.BasePage import BasePage
from config.config import TestData


class SearchFlight(BasePage):
    clickSourcePlace = (By.XPATH,
                   "//div[@class='zX8lIf T7vppb P0ukfb TFC9me PRvvEd S7G7Bc Otspu']//div[@class='v0tSxb SOcuWe']//div[@class='dvO2xc k0gFV']//div//div[@class='V00Bye ESCxub KckZb']")
    SourcePlace = (By.XPATH, "//input[@aria-label='Where from?']")
    DestinationPlace = (By.XPATH, "//input[@aria-label='Where to?']")
    clickStartDate= (By.XPATH, "//div[@class='uNiB1 iLjaEf']//div//input[@placeholder='Departure date']")
    StartDate = (By.XPATH, "//div[@class='X4feqd wDt51d']//input[@placeholder='Departure date']")
    clickEndDate= (By.XPATH, "//div[contains(@class,'uNiB1 iLjaEf')]//div//input[contains(@placeholder,'Return date')]")
    EndDate = (By.XPATH, "//div[contains(@class,'X4feqd wDt51d')]//input[contains(@placeholder,'Return date')]")
    SearchButton = (By.XPATH,
                    "//button[contains(@class,'VfPpkd-LgbsSe VfPpkd-LgbsSe-OWXEXe-k8QpJ VfPpkd-LgbsSe-OWXEXe-Bz112c-M1Soyc nCP5yc AjY5Oe')]//div[contains(@class,'VfPpkd-Jh9lGc')]")
    BestDepartingSearch = (By.XPATH, "//div[@jscontroller='ELzlhf']")
    NoResult = (By.XPATH, "//p[@class='X3FoHd']")
    DropDownSearch = (By.XPATH, "//div[@class='w1ZvBc']")
    clickDestinationPlace = (By.XPATH, "//div[@class='zX8lIf T7vppb P0ukfb TFC9me PRvvEd WKeVIb Otspu']//div[@class='v0tSxb SOcuWe']//div[@class='dvO2xc k0gFV']//div//div[@class='V00Bye ESCxub KckZb']")
    DestinationDropDown = (By.XPATH, "//div[@class='zsRT0d']")
    btnDone = (By.XPATH, "//div[@class='WXaAwc']")
    DepartingFlightList = (By.XPATH, "(//h3[contains(text(),'flights')])[1]")


    def __init__(self, driver):
        super().__init__(driver)
        self.driver.get(TestData.BASE_URL)
        self.driver.maximize_window()
        self.driver.delete_all_cookies()

    def set_sourcedestination_place(self, source, destination):
        self.click_element(self.clickSourcePlace)
        self.set_text(self.SourcePlace, source)
        time.sleep(2)
        self.click_element(self.DropDownSearch)
        self.click_element(self.clickDestinationPlace)
        self.set_text(self.DestinationPlace, destination)
        time.sleep(2)
        self.click_element(self.DropDownSearch)

    def enter_startandenddate(self, strip, startdate, enddate):
        if strip == "Round trip":
            self.click_element(self.clickStartDate)
            for element in range(0, len(startdate)):
                WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.StartDate)).send_keys(
                    Keys.BACKSPACE)
        self.set_text(self.StartDate, startdate)
            #self.click_element(self.btnDone)
            #WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.BestDepartingSearch))
           # self.click_element(self.clickEndDate)
        for element in range(0, len(enddate)):
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.EndDate)).send_keys(Keys.BACKSPACE)
        self.set_text(self.EndDate, enddate)
        time.sleep(1)
        self.click_element(self.btnDone)

        if strip == "One way":
            self.click_element(self.clickStartDate)
            self.set_text(self.StartDate, startdate)
            time.sleep(2)
            self.click_element(self.btnDone)

    def click_search_button(self):
        try:
            self.click_element(self.SearchButton)
        except:
            return False
        return True

    def search_positive_validation(self):
        WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.DepartingFlightList))
        self.is_element_displayed(self.DepartingFlightList)

