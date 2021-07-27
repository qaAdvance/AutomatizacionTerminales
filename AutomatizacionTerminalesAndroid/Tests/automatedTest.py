import pytest
import unittest
from selenium import webdriver
from AutomatizacionTerminalesAndroid.Classes.base import Base
from AutomatizacionTerminalesAndroid.Classes.installmentsPage import InstallmentsPage
from AutomatizacionTerminalesAndroid.Classes.mainPage import MainPage
from AutomatizacionTerminalesAndroid.Classes.ticketsPage import TicketPage
from appium import webdriver


class TestCases:


    def setup(self):
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', Base.return_base())
        driver = self.driver
        return driver

    def test_case_buy(self):
        driver = self.setup()
        self.installments_page = InstallmentsPage(driver)
        self.main_page = MainPage(driver)
        self.tickets_page = TicketPage(driver)
        self.main_page.enter_amount("1234")
        self.main_page.payment_option("card")
        self.tickets_page.print_client_ticket()
        self.tickets_page.btn_continue()
        self.tickets_page.btn_finish()

if __name__ == '__main__':
    pytest.main(["-v", "--alluredir=/tmp/my_allure_results", "C:/Users/lucas.hartman/Documents/Lucas/Tsoft/prisma/AutomatizacionTerminales/AutomatizacionTerminalesAndroid/Tests/automatedTest.py"])




