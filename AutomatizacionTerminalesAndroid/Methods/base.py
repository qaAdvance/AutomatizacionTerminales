from appium import webdriver


class Base:

    def __init__(self):
        self.terminal_newland = {
            "platformName": "Android",
            "platformVersion": "5.1.1",
            "deviceName": "msm8909",
            "automationName": "UiAutomator2",
        }
        self.driver = webdriver

    def init_driver(self, server_appium):
        self.driver = webdriver.Remote(server_appium, self.terminal_newland)
        return self.driver

    def return_base(self):
        return self.terminal_newland
