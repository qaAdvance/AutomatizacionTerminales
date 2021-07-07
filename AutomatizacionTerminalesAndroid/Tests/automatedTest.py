import unittest
from AutomatizacionTerminalesAndroid.Classes.base import Base
from AutomatizacionTerminalesAndroid.Classes.installmentsPage import InstallmentsPage
from AutomatizacionTerminalesAndroid.Classes.mainPage import MainPage
from AutomatizacionTerminalesAndroid.Classes.ticketsPage import TicketPage
from appium import webdriver


class TerminalTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', Base.return_base(Base()))
        self.installments_page = InstallmentsPage(self.driver)
        self.main_page = MainPage(self.driver)
        self.tickets_page = TicketPage(self.driver)

    def test_buy(self):
        self.main_page.ingresar_monto('1234')
        self.main_page.tipo_de_pago('tarjeta')
        self.installments_page.installments_value("card", "6")
        self.tickets_page.print_client_ticket()
        self.tickets_page.continue_button()
        self.tickets_page.finish_button()

    def tearDown(self):
        print("finalizado")


if __name__ == '__main__':
    unittest.main()