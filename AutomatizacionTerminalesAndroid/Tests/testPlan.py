import pytest
from Methods.base import Base
from Methods.inputs import Inputs


driver = Base.init_driver('http://127.0.0.1:4723/wd/hub')
inputs = Inputs(driver)


class TestCases:

    @pytest.mark.parametrize("amount, option, plots, expected_result", [
        ("1000", "card", "3", True),
    ])
    def test_case_ctls_buy(self, amount, option, plots, expected_result):
        assert inputs.payment_option(amount, option) == expected_result
        assert inputs.installments_value(option, plots) == expected_result
        assert inputs.print_client_ticket() == expected_result
        assert inputs.continue_button() == expected_result
        assert inputs.finish_button() == expected_result


if __name__ == '__main__':
    pytest.main(["-v", "--alluredir=/tmp/my_allure_results", "C:/Users/jagutierrez/Documents/GitHub/AutomatizacionTerminales/AutomatizacionTerminalesAndroid/Tests/testPlan.py"])
