import pytest
from Methods.base import Base
from Methods.inputs import Inputs
from appium import webdriver

#Funcion SetUp

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', Base.return_base(Base()))
inputs = Inputs(driver)


class TestCases:
    ''' @pytest.mark.parametrize("amount, option, plots, card_number, expiration_date, cvv, expected_result", [
        ("1000", "card", "3", "4507990000001026","0325", "830", True),
    ])'''
    def test_case_ctls_buy(self):
        inputs.payment_option("1000", "card")
        inputs.manually_enter("4507990000001026")
        inputs.enter_expiration_date("03/25")
        inputs.installments_value("card", "3")
        inputs.enter_cvv("830")
        inputs.print_client_ticket()
        inputs.continue_button()
        inputs.finish_button()


if __name__ == '__main__':
    pytest.main(["-v", "--alluredir=/tmp/my_allure_results", "C:/Users/jagutierrez/Documents/GitHub/AutomatizacionTerminales/AutomatizacionTerminalesAndroid/Tests/testPlan.py"])
