import time
import unittest
from base import Base
from installmentsPage import InstallmentsPage
from appium import webdriver


class TerminalTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', Base.return_base(Base()))
        self.installments_page = InstallmentsPage(self.driver)

    def test_buy(self):
        self.driver.find_element_by_id("br.com.phoebus.paystore.platform.newland:id/btn_one").click()
        self.driver.find_element_by_id("br.com.phoebus.paystore.platform.newland:id/btn_one").click()
        self.driver.find_element_by_id("br.com.phoebus.paystore.platform.newland:id/btn_one").click()
        self.driver.find_element_by_id("br.com.phoebus.paystore.platform.newland:id/btn_one").click()
        self.driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.view.View/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout[5]/android.widget.FrameLayout/android.widget.LinearLayout").click()
        time.sleep(10)
        self.installments_page.installments_value("card", "7")
        time.sleep(2)

    def tearDown(self):
        print("finalizado")


if __name__ == '__main__':
    unittest.main()