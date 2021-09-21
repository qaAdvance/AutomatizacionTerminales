import pytest
from AutomatizacionTerminalesAndroid.Methods.base import Base
from AutomatizacionTerminalesAndroid.Methods.inputs import Inputs
from appium import webdriver

#Funcion SetUp

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', Base.return_base(Base()))
inputs = Inputs(driver)


class TestCases:

    def test_case_token_init(self):
        '''assert inputs.enter_setup() is True'''
        assert inputs.token_setup(87609824) is True
        assert inputs.recover_transactions("yes") is True
        assert inputs.enter_supervisor_pass("111111") is True
        assert inputs.check_screen_main_page() is True


if __name__ == '__main__':
    pytest.main(["-v", "--alluredir=/tmp/my_allure_results", "C:/PythonFramework/AutomatizacionTerminalesAndroid/Tests/BetaTestInicializacion.py"])
