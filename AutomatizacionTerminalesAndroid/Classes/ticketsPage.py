import json
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

a = open("../Btn_mapping/pantalla_ticket.json", "r")
b = a.read()
ticketPageButtons = json.loads(b)


class TicketPage:

    def __init__(self, my_driver):
        self.driver = my_driver
        self.btn_print_ticket = (By.ID, ticketPageButtons["btn_imprimir_ticket"]["value_id"])
        self.btn_continue = (By.ID, ticketPageButtons["btn_continuar"]["value_id"])
        self.btn_finish = (By.ID, ticketPageButtons["btn_terminar"]["value_id"])
        self.print_title = (By.ID, ticketPageButtons["titulo_de_ventana"]["value_xpath"])

    def print_client_ticket(self):
        try:
            element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.btn_print_ticket))
            self.driver.find_element(*self.btn_print_ticket).click()
        except:
            print('No se encuentro el boton de imprimir ticket')

    def continue_button(self):
        try:
            self.check_screen_total_pay()
            self.driver.find_element(*self.btn_continue).click()
        except:
            print('No se encuentro el boton continuar')

    def finish_button(self):
        try:
            element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.btn_finish))
            self.driver.find_element(*self.btn_finish).click()
        except:
            print('No se encuentro el boton de terminar')

    def check_screen_total_pay(self):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.print_title))
        except:
            print("No estas en la pantalla de pago total")