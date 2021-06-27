import pytest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Pages import ReadExcel
from Pages.SearchFlight import SearchFlight
from Test.Test_Base import BaseTest
from config.config import TestData


class Test_Round_Trip_Validation(BaseTest):

    # Test Cases

    # def test_search_flight(self):
    #     self.searchflight = SearchFlight(self.driver)
    #     self.searchflight.set_sourcedestination_place("BBI", "KUU")
    #     self.searchflight.enter_startandenddate("Round trip", "Mon, Jul 12", "Fri, Jul 16")
    #     WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.searchflight.DepartingFlightList))
    #     self.searchflight.search_positive_validation()

    def test_search_flight(self):
        self.searchflight = SearchFlight(self.driver)
        path = "Resource/InputData.xlsx"
        rows = ReadExcel.getRowCount(path, "Positive_Validation")

        for r in range(2, rows + 1):
            source = ReadExcel.readData(path, "Positive_Validation", r, 1)
            destination = ReadExcel.readData(path, "Positive_Validation", r, 2)
            trip = ReadExcel.readData(path, "Positive_Validation", r, 3)
            startdate = ReadExcel.readData(path, "Positive_Validation", r, 4)
            enddate = ReadExcel.readData(path, "Positive_Validation", r, 5)
            self.searchflight.set_sourcedestination_place(source, destination)
            self.searchflight.enter_startandenddate(trip, startdate, enddate)
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.searchflight.DepartingFlightList))
            self.searchflight.search_positive_validation()


