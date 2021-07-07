class Base:

    def __init__(self):
        self.desire_cap = {
            "platformName": "Android",
            "platformVersion": "5.1.1",
            "deviceName": "msm8909",
            "automationName": "UiAutomator2",
            "appPackage": "br.com.phoebus.paystore.platform.newland",
            "appActivity": "br.com.phoebus.android.platform.ui.activity.MainActivity"
        }

    def return_base(self):
        return self.desire_cap
