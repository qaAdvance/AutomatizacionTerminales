import pytest
<<<<<<< HEAD
from AutomatizacionTerminalesAndroid.Classes.base import Base
from AutomatizacionTerminalesAndroid.Classes.installmentsPage import InstallmentsPage
from AutomatizacionTerminalesAndroid.Classes.mainPage import MainPage
from AutomatizacionTerminalesAndroid.Classes.ticketsPage import TicketPage
from appium import webdriver


class TestCases:


    def setup(self):
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', Base.return_base(Base()))
        driver = self.driver
        return driver

    def test_case_buy(self):
        driver = self.setup()
        self.installments_page = InstallmentsPage(driver)
        self.main_page = MainPage(driver)
        self.tickets_page = TicketPage(driver)
        self.main_page.enter_amount("1234")
        assert self.main_page.payment_option("card") is True


if __name__ == '__main__':
    pytest.main(["-v", "--alluredir=/tmp/my_allure_results", "C:/Users/lucas.hartman/Documents/Lucas/Tsoft/prisma/AutomatizacionTerminales/AutomatizacionTerminalesAndroid/Tests/automatedTest.py"])



=======
from Methods.base import Base
from Methods.inputs import Inputs
from appium import webdriver


class TestCase:
    def set_up(self):
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', Base.return_base(Base()))
        self.inputs = Inputs(self.driver)

    def test_case_enter_amount(self):
        assert inputs.enter_amount("1234") is True

    def test_case_payment_option(self):
        assert inputs.payment_option("card") is True

    def test_case_plots(self):
        assert inputs.installments_value("card", "3") is True

    def test_case_print_ticket(self):
        assert inputs.print_client_ticket() is True

    def test_case_continue_button(self):
        assert inputs.continue_button() is True

    def test_case_finish_button(self):
        assert inputs.finish_button() is True


if __name__ == '__main__':
    pytest.main(["-v", "--alluredir=/tmp/my_allure_results", "C:/Users/jagutierrez/Documents/GitHub/AutomatizacionTerminales/AutomatizacionTerminalesAndroid/Tests/automatedTest.py"])
>>>>>>> Javier

