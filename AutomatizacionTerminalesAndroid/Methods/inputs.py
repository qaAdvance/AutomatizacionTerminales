from AutomatizacionTerminalesAndroid.Methods.complementary import Complementary
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from appium.webdriver.common.touch_action import TouchAction
import time


class Inputs:

    def __init__(self, my_driver):
        '''Inicializacion de diccionarios con mapeo de botones'''
        main_page_buttons = Complementary.read_json("../Resources/pagina_principal.json")
        installments_page_buttons = Complementary.read_json("../Resources/pantalla_cuotas.json")
        payment_page_buttons = Complementary.read_json("../Resources/pantalla_pago.json")
        ticket_page_buttons = Complementary.read_json("../Resources/pantalla_ticket.json")
        function_menu = Complementary.read_json("../Resources/pestaña_funciones.json")
        function_option_menu = Complementary.read_json("../Resources/menu_funciones.json")
        paystore_token_menu = Complementary.read_json("../Resources/pantalla_paystore_token.json")
        self.driver = my_driver
        ''' botones Payment Page '''
        self.btn_manual_enter = (By.ID, payment_page_buttons["btn_ingreso_manual"]["value_id"])
        self.btn_enter_card_number = (By.ID, payment_page_buttons["numero_de_tarjeta"]["value_id"])
        self.btn_text_screen = (By.ID, payment_page_buttons["mensaje_en_pantalla"]["value_id"])
        self.btn_expiration_date = (By.XPATH, payment_page_buttons["expiration_date_box"]["value_xpath"])
        self.btn_cvv_code = (By.XPATH, payment_page_buttons["numero_cvv"]["value_xpath"])
        self.btn_accept_card_number = (By.XPATH, payment_page_buttons["btn_aceptar_card_number"]["value_xpath"])
        self.btn_accept_exp_date = (By.XPATH, payment_page_buttons["btn_aceptar_exp_date"]["value_xpath"])
        self.btn_accept_cvv = (By.XPATH, payment_page_buttons["btn_aceptar_cvv"]["value_xpath"])
        ''' botones Ticket Page '''
        self.print_title = (By.ID, ticket_page_buttons["titulo_de_ventana"]["value_xpath"])
        self.btn_print_ticket = (By.ID, ticket_page_buttons["btn_imprimir_ticket"]["value_id"])
        self.btn_continue = (By.ID, ticket_page_buttons["btn_continuar"]["value_id"])
        self.btn_finish = (By.ID, ticket_page_buttons["btn_terminar"]["value_id"])
        '''botones main Page'''
        self.btn_0 = (By.ID, main_page_buttons["btn_numerico_cero"]["value_id"])
        self.btn_1 = (By.ID, main_page_buttons["btn_numerico_uno"]["value_id"])
        self.btn_2 = (By.ID, main_page_buttons["btn_numerico_dos"]["value_id"])
        self.btn_3 = (By.ID, main_page_buttons["btn_numerico_tres"]["value_id"])
        self.btn_4 = (By.ID, main_page_buttons["btn_numerico_cuatro"]["value_id"])
        self.btn_5 = (By.ID, main_page_buttons["btn_numerico_cinco"]["value_id"])
        self.btn_6 = (By.ID, main_page_buttons["btn_numerico_seis"]["value_id"])
        self.btn_7 = (By.ID, main_page_buttons["btn_numerico_siete"]["value_id"])
        self.btn_8 = (By.ID, main_page_buttons["btn_numerico_ocho"]["value_id"])
        self.btn_9 = (By.ID, main_page_buttons["btn_numerico_nueve"]["value_id"])
        self.btn_buy = (By.XPATH, main_page_buttons["btn_cobrar"]["value_xpath"])
        self.btn_qr = (By.ID, main_page_buttons["btn_generar_qr"]["value_id"])
        self.btn_split = (By.ID, main_page_buttons["btn_pago_dividido"]["value_id"])
        self.clean_btn_c = Complementary.clean_quotation_marks(main_page_buttons["btn_activar_calculadora"]["value_xpath"])
        self.btn_calculator = (By.XPATH, self.clean_btn_c)
        self.btn_side_menu = (By.CLASS_NAME, main_page_buttons["btn_menu_lateral"]["value_accessibility_id"])
        self.btn_delete = (By.ID, main_page_buttons["btn_borrar_numero"]["value_id"])
        '''botones Installent Page'''
        self.btn_accept = (By.ID, installments_page_buttons["btn_aceptar"]["value_id"])
        self.btn_three_plots = (By.ID, installments_page_buttons["btn_tres_cuotas"]["value_id"])
        self.btn_six_plots = (By.ID, installments_page_buttons["btn_seis_cuotas"]["value_id"])
        self.btn_twelve_plots = (By.ID, installments_page_buttons["btn_doce_cuotas"]["value_id"])
        self.btn_enter_plots = (By.ID, installments_page_buttons["btn_ingresar_cuotas"]["value_id"])
        self.btn_accept_qr = (By.ID, installments_page_buttons["btn_aceptar"]["value_id_qr"])
        self.btn_three_plots_qr = (By.ID, installments_page_buttons["btn_tres_cuotas"]["value_id_qr"])
        self.btn_six_plots_qr = (By.ID, installments_page_buttons["btn_seis_cuotas"]["value_id_qr"])
        self.btn_twelve_plots_qr = (By.ID, installments_page_buttons["btn_doce_cuotas"]["value_id_qr"])
        self.btn_enter_plots_qr = (By.ID, installments_page_buttons["btn_ingresar_cuotas"]["value_id_qr"])
        '''botones Functions Panel Menu'''
        self.btn_merchant_data = (By.XPATH, function_menu["btn_datos_del_establecimiento"]["value_xpath"])
        self.btn_card_data = (By.XPATH, function_menu["btn_marcas_de_tarjetas"]["value_xpath"])
        self.btn_my_apps = (By.XPATH, function_menu["btn_mis_aplicaciones"]["value_xpath"])
        self.btn_functions = (By.XPATH, function_menu["btn_funciones"]["value_xpath"])
        self.btn_annulments_refunds = (By.XPATH, function_menu["btn_anulacion/devolucion"]["value_xpath"])
        self.btn_close_batch = (By.XPATH, function_menu["btn_cierre_de_lote"]["value_xpath"])
        self.btn_reports = (By.XPATH, function_menu["btn_informes"]["value_xpath"])
        self.btn_passwords = (By.XPATH, function_menu["btn_contrasenas"]["value_xpath"])
        self.btn_configurations = (By.XPATH, function_menu["btn_configuraciones"]["value_xpath"])
        self.btn_factory_reset = (By.XPATH, function_menu["btn_restablecer_terminal"]["value_xpath"])
        '''botones Functions Menu'''
        self.title = (By.PARTIAL_LINK_TEXT, "Funciones")
        self.option_1 = (function_option_menu["option_1"])
        self.option_2 = (function_option_menu["option_2"])
        self.option_3 = (function_option_menu["option_3"])
        self.option_4 = (function_option_menu["option_4"])
        self.option_5 = (function_option_menu["option_5"])
        self.option_6 = (function_option_menu["option_6"])
        self.option_7 = (function_option_menu["option_7"])
        self.option_back = (function_option_menu["option_back"])
        """Pantalla de paystore para ingreso de token"""
        self.btn_settings = (By.XPATH, paystore_token_menu["btn_settings"]["value_xpath"])
        self.btn_start_setup = (By.XPATH, paystore_token_menu["btn_start_setup"]["value_xpath"])
        self.token_text_box = (By.XPATH, paystore_token_menu["btn_token_text_box"]["value_xpath"])
        self.btn_check = (paystore_token_menu["btn_check"])
        self.btn_recover_transactions_yes = (By.XPATH, paystore_token_menu["btn_recover_transactions_yes"]["value_xpath"])
        self.btn_recover_transactions_no = (By.XPATH, paystore_token_menu["btn_recover_transactions_no"]["value_xpath"])
        self.btn_recover_transaction_finish = (By.XPATH, paystore_token_menu["btn_recover_transaction_finish"]["value_xpath"])
        self.btn_password_text_box = (By.XPATH, paystore_token_menu["btn_password_text_box"]["value_xpath"])
        self.btn_password_confirm_text_box = (By.XPATH, paystore_token_menu["btn_password_confirm_text_box"]["value_xpath"])
        self.btn_accept_pass = (By.XPATH, paystore_token_menu["btn_accept_pass"]["value_xpath"])

    '''Compra general'''

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

    '''Compra manual'''

    def manually_enter(self, card_number):
        try:
            btn_manual_enter_check = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(self.btn_manual_enter))
            self.driver.find_element(*self.btn_manual_enter).click()
            btn_manual_card_check = WebDriverWait(self.driver, 15).until(EC.presence_of_element_located(self.btn_enter_card_number))
            self.driver.find_element(*self.btn_enter_card_number).send_keys(card_number)
            self.check_accept_card_number()
            return True
        except:
            print("Not in payments page")
            return False

    def enter_expiration_date(self, expiration_date):
        try:
            btn_manual_enter_check = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located(self.btn_expiration_date))
            self.driver.find_element(*self.btn_expiration_date).send_keys(expiration_date)
            self.check_accept_exp_date()
            return True
        except:
            print("can't find expiration date box")
            return False

    def enter_cvv(self, cvv):
        try:
            btn_manual_enter_check = WebDriverWait(self.driver, 15).until(
                EC.presence_of_element_located(self.btn_cvv_code))
            self.driver.find_element(*self.btn_cvv_code).send_keys(cvv)
            self.check_accept_cvv()
            return True
        except AssertionError:
            print("can't find cvv enter box")
            return False

    '''Compra credito'''

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
                    self.driver.find_element(*self.btn_enter_plots).clear()
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
                    self.driver.find_element(*self.btn_enter_plots_qr).clear()
                    self.driver.find_element(*self.btn_enter_plots_qr).send_keys(installment_value)
                    self.driver.find_element(*self.btn_accept_qr).click()
            else:
                print("try:\nBuy_type equal to card or qr\ninstallment_value between 1 to 99")
            return True
        except:
            print('No se encuentra la pantalla de coutas')
            return False

    '''checks'''

    def check_screen_main_page(self):
        try:
            element = WebDriverWait(self.driver, 120).until(EC.visibility_of_element_located(self.btn_buy))
            return True
        except:
            print("You're not in main page")
            return False

    def check_accept_card_number(self):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.btn_accept_card_number))
            self.driver.find_element(*self.btn_accept_card_number).click()
        except:
            print("can´t find accept button in card number")

    def check_accept_exp_date(self):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.btn_accept_exp_date))
            self.driver.find_element(*self.btn_accept_exp_date).click()
        except:
            print("can´t find accept button in expiration date")

    def check_accept_cvv(self):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.btn_accept_cvv))
            self.driver.find_element(*self.btn_accept_cvv).click()
        except:
            print("can´t find accept button in cvv code")

    def check_screen_total_pay(self):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(self.print_title))
        except:
            print("No estas en la pantalla de pago total")

    '''Complementarias'''

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

    def touch_screen(self, x, y):
        time.sleep(2)
        TouchAction(self.driver).tap(x=x, y=y).perform()

    def token_setup(self, token):
        try:
            self.driver.find_element(*self.token_text_box).send_keys(token)
            self.touch_screen(self.btn_check["value_x"], self.btn_check["value_y"])
            return True
        except:
            print("Not in token entry screen")
            return False

    '''Funciones / Interacciones'''

    def swipe_open_side_menu(self):
        try:
            self.check_screen_main_page()
            self.driver.swipe(start_x=20, start_y=650, end_x=450, end_y=650, duration=800)
            return True
        except:
            print("couldn't swipe to open side menu")
            return False

    def open_functions_options(self):
        try:
            element = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable(self.btn_functions))
            self.driver.find_element(*self.btn_functions).click()
            return True
        except:
            print("Function option button is not present")
            return False

    def select_function_option(self, option_number):
        time.sleep(5)
        if option_number == 1:
            TouchAction(self.driver).tap(x=self.option_1["value_x"], y=self.option_1["value_y"]).perform()
            time.sleep(5)
        elif option_number == 2:
            TouchAction(self.driver).tap(x=self.option_2["value_x"], y=self.option_2["value_y"]).perform()
        elif option_number == 3:
            TouchAction(self.driver).tap(x=self.option_3["value_x"], y=self.option_3["value_y"]).perform()
        elif option_number == 4:
            TouchAction(self.driver).tap(x=self.option_4["value_x"], y=self.option_4["value_y"]).perform()
        elif option_number == 5:
            TouchAction(self.driver).tap(x=self.option_5["value_x"], y=self.option_5["value_y"]).perform()
        elif option_number == 6:
            TouchAction(self.driver).tap(x=self.option_6["value_x"], y=self.option_6["value_y"]).perform()
        elif option_number == 7:
            TouchAction(self.driver).tap(x=self.option_7["value_x"], y=self.option_7["value_y"]).perform()
        elif option_number == 8:
            time.sleep(8)
            TouchAction(self.driver).tap(x=self.option_back["value_x"], y=self.option_back["value_y"]).perform()

    def open_calculator(self):
        try:
            element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(self.btn_calculator))
            self.driver.find_element(*self.btn_calculator).click()
            return True
        except:
            print("Calculator button is not present")
            return False

    '''Cierre de lote'''

    '''Funciones para ingreso de token'''

    def enter_setup(self):
        try:
            element = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self.btn_start_setup))
            self.driver.find_element(*self.btn_start_setup).click()
            return True
        except:
            print("Not in token screen")
            return False

    def recover_transactions(self, answer):
        try:
            element = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self.btn_recover_transactions_yes))
            if answer == "yes" or "y":
                self.driver.find_element(*self.btn_recover_transactions_yes).click()
            elif answer == "no" or "n":
                self.driver.find_element(*self.btn_recover_transactions_no).click()

            element = WebDriverWait(self.driver,30).until(EC.element_to_be_clickable(self.btn_recover_transaction_finish))
            self.driver.find_element(*self.btn_recover_transaction_finish).click()
            return True
        except:
            print("Not in recover transaction option")
            return False

    def enter_supervisor_pass(self, password):
        try:
            element = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located(self.btn_password_text_box))
            self.driver.find_element(*self.btn_password_text_box).clear()
            self.driver.find_element(*self.btn_password_text_box).send_keys(password)
            element = WebDriverWait(self.driver, 30).until(
                EC.presence_of_element_located(self.btn_password_confirm_text_box))
            self.driver.find_element(*self.btn_password_text_box).clear()
            self.driver.find_element(*self.btn_password_confirm_text_box).send_keys(password)
            element = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable(self.btn_accept_pass))
            self.driver.find_element(*self.btn_accept_pass).click()
            return True
        except:
            print("not in supervisor password setup")
            return False
