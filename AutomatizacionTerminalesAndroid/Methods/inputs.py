import json
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time

'''Crear funcion de lectura de Jsons'''

a = open("../Resources/pantalla_pago.json", "r")
b = a.read()
PaymentPageButtons = json.loads(b)

a = open("../Resources/pantalla_ticket.json", "r")
b = a.read()
ticketPageButtons = json.loads(b)

a = open("../Resources/pagina_principal.json", "r")
b = a.read()
mainPageButtons = json.loads(b)

a = open("../Resources/pantalla_cuotas.json", "r")
b = a.read()
InstallmentsPageButtons = json.loads(b)


class Inputs:

    def __init__(self, my_driver):
        self.driver = my_driver
        ''' botones Payment Page '''
        self.btn_manual_enter = (By.ID, PaymentPageButtons["btn_ingreso_manual"]["value_id"])
        self.btn_enter_card_number = (By.ID, PaymentPageButtons["numero_de_tarjeta"]["value_id"])
        self.btn_text_screen = (By.ID, PaymentPageButtons["mensaje_en_pantalla"]["value_id"])
        self.btn_accept_popup = (By.ID, PaymentPageButtons["btn_aceptar_popup"]["value_xpath"])
        self.btn_expiration_date = (By.ID, PaymentPageButtons["expiration_date_box"]["value_id"])
        self.btn_cvv_code = (By.ID, PaymentPageButtons["numero_cvv"]["value_id"])
        ''' botones Ticket Page '''
        self.print_title = (By.ID, ticketPageButtons["titulo_de_ventana"]["value_xpath"])
        self.btn_print_ticket = (By.ID, ticketPageButtons["btn_imprimir_ticket"]["value_id"])
        self.btn_continue = (By.ID, ticketPageButtons["btn_continuar"]["value_id"])
        self.btn_finish = (By.ID, ticketPageButtons["btn_terminar"]["value_id"])
        '''botones main Page'''
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
        '''botones Installent Page'''
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


    ''' VER PORQUE EL BOTON ACEPTAR NO SE ENCUNETRA'''
    def manually_enter(self, card_number):
        try:
            btn_manual_enter_check = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(self.btn_manual_enter))
            self.driver.find_element(*self.btn_manual_enter).click()
            btn_manual_card_check = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(self.btn_enter_card_number))
            self.driver.find_element(*self.btn_enter_card_number).send_keys(card_number)
            self.check_accept_popup_button()
            return True
        except:
            print("Not in payments page")
            return False

    def enter_expiration_date(self, expiration_date):
        try:
            btn_manual_enter_check = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(self.btn_expiration_date))
            self.driver.find_element(*self.btn_expiration_date).send_keys(expiration_date)
            self.check_accept_popup_button()

            return True
        except:
            print("can't find expiration date box")
            return False

    def enter_cvv(self, cvv):
        try:
            btn_manual_enter_check = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(self.btn_cvv_code))
            self.driver.find_element(*self.btn_cvv_code).send_keys(cvv)
            self.check_accept_popup_button()

            return True
        except AssertionError:
            print("can't find cvv enter box")
            return False

    def check_accept_popup_button(self):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.btn_accept_popup))
            self.driver.find_element(*self.btn_accept_popup).click()
        except:
            print("No estas en la pantalla de pago total")

    def print_client_ticket(self):
        try:
            element = WebDriverWait(self.driver, 30).until(EC.visibility_of_element_located(self.btn_print_ticket))
            self.driver.find_element(*self.btn_print_ticket).click()
            return True
        except:
            print('No se encuentro el boton de imprimir ticket')
            return False

    def continue_button(self):
        try:
            self.check_screen_total_pay()
            self.driver.find_element(*self.btn_continue).click()
            return True
        except:
            print('No se encuentro el boton continuar')
            return False

    def finish_button(self):
        try:
            element = WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(self.btn_finish))
            self.driver.find_element(*self.btn_finish).click()
            return True
        except:
            print('No se encuentro el boton de terminar')
            return False

    def check_screen_total_pay(self):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.print_title))
        except:
            print("No estas en la pantalla de pago total")

    def enter_amount(self, number):
        try:
            self.check_screen_main_page()
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
            return True
        except:
            print("No se pudo ingresar el monto")
            return False

    def payment_option(self, amount, payment_option):
        self.enter_amount(amount)
        if payment_option == "card":
            try:
                element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.btn_buy))
                self.driver.find_element(*self.btn_buy).click()
                return True
            except:
                return False
        elif payment_option == "qr":
            try:
                element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.btn_qr))
                self.driver.find_element(*self.btn_qr).click()
                return True
            except:
                return False
        elif payment_option == "split":
            try:
                element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.btn_split))
                self.driver.find_element(*self.btn_split).click()
                return True
            except:
                return False
        else:
            print("try:\ncard\nqr\nsplit\nAs payment option")

    def installments_value(self, buy_type, installment_value):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.btn_accept))
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
            else:
                print("try:\nBuy_type equal to card or qr\ninstallment_value between 1 to 99")
            return True
        except:
            print('No se encuentra la pantalla de coutas')
            return False

    def check_screen_main_page(self):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.btn_buy))
        except:
            print("No estas en la pantalla de pago total")