from AutomatizacionTerminalesAndroid.Methods.complementary import Complementary
from selenium.webdriver.common.by import By
from AutomatizacionTerminalesAndroid.Methods.base import Base
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


function_option_menu = Complementary.read_json("../Resources/menu_funciones.json")
main_page_buttons = Complementary.read_json("../Resources/pagina_principal.json")
prueba = Complementary.read_json("../Resources/pantalla_paystore_token.json")
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', Base.return_base(Base()))

input = (By.XPATH, prueba["btn_token_text_box"]["value_xpath"])
print(input)

driver.find_element(*input).send_keys("12345678")

