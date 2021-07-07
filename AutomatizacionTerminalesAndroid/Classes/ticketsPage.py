import json
from selenium.webdriver.common.by import By

a = open("../Btn_mapping/pantalla_ticket.json", "r")
b = a.read()
ticketPageButtons = json.loads(b)


class TicketPage:

    def __init__(self, my_driver):
        self.driver = my_driver
        self.btn_print_ticket = (By.ID, ticketPageButtons["btn_imprimir_ticket"]["value_id"])
        self.btn_continue = (By.ID, ticketPageButtons["btn_continuar"]["value_id"])
        self.btn_finish = (By.ID, ticketPageButtons["btn_terminar"]["value_id"])

    def print_client_ticket(self):
        self.driver.find_element(*self.btn_print_ticket).click()

    def continue_button(self):
        self.driver.find_element(*self.btn_continue).click()

    def finish_button(self):
        self.driver.find_element(*self.btn_finish).click()
