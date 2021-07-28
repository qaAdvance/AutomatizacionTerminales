import pytest
from Methods.base import Base
from Methods.inputs import Inputs
from appium import webdriver

#Funcion SetUp

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', Base.return_base(Base()))
inputs = Inputs(driver)


class TestCases:
    @pytest.mark.parametrize("amount, option, plots, card_number, expiration_date, cvv, expected_result", [
        ("1000", "card", "1", "4507990000001026","03/25", "830", True),
        ("1100", "card", "3", "5300589000846764","04/27", "830", True),
    ])
    def test_case_ctls_buy(self, amount, option, plots, card_number, expiration_date, cvv, expected_result):
        assert inputs.payment_option(amount, option) == expected_result
        assert inputs.manually_enter(card_number) == expected_result
        assert inputs.enter_expiration_date(expiration_date) == expected_result
        assert inputs.installments_value(option, plots) == expected_result
        assert inputs.enter_cvv(cvv) == expected_result
        assert inputs.print_client_ticket() == expected_result
        assert inputs.continue_button() == expected_result
        assert inputs.finish_button() == expected_result


if __name__ == '__main__':
    pytest.main(["-v", "--alluredir=/tmp/my_allure_results", "C:/Users/jagutierrez/Documents/GitHub/AutomatizacionTerminales/AutomatizacionTerminalesAndroid/Tests/testPlan.py"])
