import  pytest

from Pages.LoginPage import LoginPage
from Test.Test_Base import BaseTest
from config.config import TestData


class Test_Login(BaseTest):

    def test_login_page_title(self):
        self.loginpage = LoginPage(self.driver)
        title= self.loginpage.get_title(TestData.Login_Page_Title)
        assert title == TestData.Login_Page_Title


    def test_login(self):
        self.loginpage = LoginPage(self.driver)
        self.loginpage.do_login(TestData.USER_NAME, TestData.PASSWORD)


