from ddt import ddt, data, file_data
from appium import webdriver
import unittest

desire_cap = {
    "platformName": "Android",
    "platformVersion": "5.1.1",
    "deviceName": "msm8909",
    "automationName": "UiAutomator2",
    "appPackage": "br.com.phoebus.paystore.platform.newland",
    "appActivity": "br.com.phoebus.android.platform.ui.activity.MainActivity"
}

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desire_cap)

uno = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.view.View/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.Button[1]')
cero = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.view.View/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout[4]/android.widget.Button')
cobrar = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.support.v4.widget.DrawerLayout/android.view.View/android.support.v4.view.ViewPager/android.widget.LinearLayout/android.widget.RelativeLayout[2]/android.widget.LinearLayout/android.widget.LinearLayout[5]/android.widget.FrameLayout/android.widget.LinearLayout')

uno.click()
cero.click()
cero.click()
cero.click()
cobrar.click()
