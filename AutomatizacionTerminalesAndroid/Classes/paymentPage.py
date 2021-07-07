import json
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait

a = open("pantalla_pago.json", "r")
b = a.read()
PaymentPageButtons = json.loads(b)


class PaymentPage:

    def __init__(self, my_driver):
        self.driver = my_driver
        self.btn_manual_enter = (By.ID, PaymentPageButtons["btn_ingreso_manual"]["value_id"])
        self.btn_enter_card_number = (By.ID, PaymentPageButtons["numero_de_tarjeta"]["value_id"])
        self.btn_text_screen = (By.ID, PaymentPageButtons["mensaje_en_pantalla"]["value_id"])
        self.btn_enter_card_number_accept = (By.ID, PaymentPageButtons["numero_tarjeta_acpetar"]["value_xpath"])

    def manually_enter(self, card_number):
        try:
            btn_manual_enter_check = WebDriverWait(self.driver, 5).until(ec.presence_of_element_located(self.btn_manual_enter))
            self.driver.find_element(*self.btn_manual_enter).click()
            self.driver.find_element(*self.btn_enter_card_number).send_keys(card_number)
            self.driver.find_element(*self.btn_enter_card_number_accept).click()

        except:
            print("Not in payments page")