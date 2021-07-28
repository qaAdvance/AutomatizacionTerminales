from appium import webdriver


class Base:

    def __init__(self):
        self.terminal_newland = {
            "platformName": "Android",
            "platformVersion": "5.1.1",
            "deviceName": "msm8909",
            "automationName": "UiAutomator2",
            "appPackage": "br.com.phoebus.paystore.platform.newland",
            "appActivity": "br.com.phoebus.android.platform.ui.activity.MainActivity"
        }

    @staticmethod
    def init_driver(self, server_appium):
        driver = webdriver.Remote(server_appium, self.terminal_newland)
        return driver
