import json
from selenium.webdriver.common.by import By

a = open("../Btn_mapping/pantalla_cuotas.json", "r")
b = a.read()
InstallmentsPageButtons = json.loads(b)


class InstallmentsPage:

    def __init__(self, my_driver):
        self.driver = my_driver
        self.btn_accept = (By.ID, InstallmentsPageButtons["btn_aceptar"]["value_id"])
        self.btn_three_plots = (By.ID, InstallmentsPageButtons["btn_tres_cuotas"]["value_id"])
        self.btn_six_plots = (By.ID, InstallmentsPageButtons["btn_seis_cuotas"]["value_id"])
        self.btn_twelve_plots = (By.ID, InstallmentsPageButtons["btn_doce_cuotas"]["value_id"])
        self.btn_enter_plots = (By.ID, InstallmentsPageButtons["btn_ingresar_cuotas"]["value_id"])
        self.btn_accept_qr = (By.ID, InstallmentsPageButtons["btn_aceptar"]["value_id_qr"])
        self.btn_three_plots_qr = (By.ID, InstallmentsPageButtons["btn_tres_cuotas"]["value_id_qr"])
        self.btn_six_plots_qr = (By.ID, InstallmentsPageButtons["btn_seis_cuotas"]["value_id_qr"])
        self.btn_twelve_plots_qr = (By.ID, InstallmentsPageButtons["btn_doce_cuotas"]["value_id_qr"])
        self.btn_enter_plots_qr = (By.ID, InstallmentsPageButtons["btn_ingresar_cuotas"]["value_id_qr"])

    def installments_value(self, buy_type, installment_value):
        if buy_type == "card":
            if installment_value == "1":
                self.driver.find_element(*self.btn_accept).click()
            elif installment_value == "3":
                self.driver.find_element(*self.btn_three_plots).click()
                self.driver.find_element(*self.btn_accept).click()
            elif installment_value == "6":
                self.driver.find_element(*self.btn_six_plots).click()
                self.driver.find_element(*self.btn_accept).click()
            elif installment_value == "12":
                self.driver.find_element(*self.btn_twelve_plots).click()
                self.driver.find_element(*self.btn_accept).click()
            else:
                self.driver.find_element(*self.btn_enter_plots).click()
                self.driver.find_element(*self.btn_enter_plots).send_keys(installment_value)
                self.driver.find_element(*self.btn_accept).click()

        elif buy_type == "qr":
            if installment_value == "1":
                self.driver.find_element(*self.btn_accept_qr).click()
            elif installment_value == "3":
                self.driver.find_element(*self.btn_three_plots_qr).click()
                self.driver.find_element(*self.btn_accept).click()
            elif installment_value == "6":
                self.driver.find_element(*self.btn_six_plots_qr).click()
                self.driver.find_element(*self.btn_accept).click()
            elif installment_value == "12":
                self.driver.find_element(*self.btn_twelve_plots_qr).click()
                self.driver.find_element(*self.btn_accept).click()
            else:
                self.driver.find_element(*self.btn_enter_plots_qr).click()
                self.driver.find_element(*self.btn_enter_plots_qr).send_keys(installment_value)
                self.driver.find_element(*self.btn_accept_qr).click()