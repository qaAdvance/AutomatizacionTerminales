import json
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

a = open("../Resources/pagina_principal.json", "r")
b = a.read()
mainPageButtons = json.loads(b)


class MainPage:

    def __init__(self, my_driver):
        self.driver = my_driver
        self.btn_0 = (By.ID, mainPageButtons["btn_numerico_cero"]["value_id"])
        self.btn_1 = (By.ID, mainPageButtons["btn_numerico_uno"]["value_id"])
        self.btn_2 = (By.ID, mainPageButtons["btn_numerico_dos"]["value_id"])
        self.btn_3 = (By.ID, mainPageButtons["btn_numerico_tres"]["value_id"])
        self.btn_4 = (By.ID, mainPageButtons["btn_numerico_cuatro"]["value_id"])
        self.btn_5 = (By.ID, mainPageButtons["btn_numerico_cinco"]["value_id"])
        self.btn_6 = (By.ID, mainPageButtons["btn_numerico_seis"]["value_id"])
        self.btn_7 = (By.ID, mainPageButtons["btn_numerico_siete"]["value_id"])
        self.btn_8 = (By.ID, mainPageButtons["btn_numerico_ocho"]["value_id"])
        self.btn_9 = (By.ID, mainPageButtons["btn_numerico_nueve"]["value_id"])
        self.btn_buy = (By.XPATH, mainPageButtons["btn_cobrar"]["value_xpath"])
        self.btn_qr = (By.ID, mainPageButtons["btn_generar_qr"]["value_id"])
        self.btn_split = (By.ID, mainPageButtons["btn_pago_dividido"]["value_id"])
        self.btn_calculator = (By.ID, mainPageButtons["btn_activar_calculadora"]["value_id"])
        self.btn_functions = (By.ID, mainPageButtons["btn_panel_funciones"]["value_id"])
        self.btn_delete = (By.ID, mainPageButtons["btn_borrar_numero"]["value_id"])

    def enter_amount(self, number):
        for n in number:
            if n == "0":
                self.driver.find_element(*self.btn_0).click()
            elif n == "1":
                self.driver.find_element(*self.btn_1).click()
            elif n == "2":
                self.driver.find_element(*self.btn_2).click()
            elif n == "3":
                self.driver.find_element(*self.btn_3).click()
            elif n == "4":
                self.driver.find_element(*self.btn_4).click()
            elif n == "5":
                self.driver.find_element(*self.btn_5).click()
            elif n == "6":
                self.driver.find_element(*self.btn_6).click()
            elif n == "7":
                self.driver.find_element(*self.btn_7).click()
            elif n == "8":
                self.driver.find_element(*self.btn_8).click()
            elif n == "9":
                self.driver.find_element(*self.btn_9).click()

    def payment_option(self, paymentOption):
        if paymentOption == "card":
            try:
                element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.btn_buy))
                self.driver.find_element(*self.btn_buy).click()
                return True
            except:
                return False
        elif paymentOption == "qr":
            try:
                element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.btn_qr))
                self.driver.find_element(*self.btn_qr).click()
                return True
            except:
                return False
        elif paymentOption == "split":
            try:
                element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.btn_split))
                self.driver.find_element(*self.btn_split).click()
                return True
            except:
                return False
        else:
            print("try:\ncard\nqr\nsplit\nAs payment option")
