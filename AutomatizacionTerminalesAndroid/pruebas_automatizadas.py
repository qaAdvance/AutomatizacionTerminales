import json
import time
from appium import webdriver
import unittest


#Mapeamos los botones desde los archivos json. Se puede editar los
#jsons en caso de que algun boton deje de existir o cambie algun valor
#para poder encontrarlo
a = open("pagina_principal.json", "r")
b = a.read()
pantallaPrincipal = json.loads(b)

a = open("pantalla_cuotas.json", "r")
b = a.read()
pantallaCuotas = json.loads(b)

a = open("pantalla_pago.json", "r")
b = a.read()
pantallaPago = json.loads(b)

a = open("pantalla_ticket.json", "r")
b = a.read()
pantallaTicket = json.loads(b)

#Inicializamos la sesion android
desire_cap = {
    "platformName": "Android",
    "platformVersion": "5.1.1",
    "deviceName": "msm8909",
    "automationName": "UiAutomator2",
    "appPackage": "br.com.phoebus.paystore.platform.newland",
    "appActivity": "br.com.phoebus.android.platform.ui.activity.MainActivity"
}
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desire_cap)

#definimos funciones
def ingresar_monto(numero):
    for n in numero:
        if n == "0":
            boton = driver.find_element_by_id(pantallaPrincipal["btn_numerico_cero"]["value_id"])
            boton.click()
        elif n == "1":
            boton = driver.find_element_by_id(pantallaPrincipal["btn_numerico_uno"]["value_id"])
            boton.click()
        elif n == "2":
            boton = driver.find_element_by_id(pantallaPrincipal["btn_numerico_dos"]["value_id"])
            boton.click()
        elif n == "3":
            boton = driver.find_element_by_id(pantallaPrincipal["btn_numerico_tres"]["value_id"])
            boton.click()
        elif n == "4":
            boton = driver.find_element_by_id(pantallaPrincipal["btn_numerico_cuatro"]["value_id"])
            boton.click()
        elif n == "5":
            boton = driver.find_element_by_id(pantallaPrincipal["btn_numerico_cinco"]["value_id"])
            boton.click()
        elif n == "6":
            boton = driver.find_element_by_id(pantallaPrincipal["btn_numerico_seis"]["value_id"])
            boton.click()
        elif n == "7":
            boton = driver.find_element_by_id(pantallaPrincipal["btn_numerico_siete"]["value_id"])
            boton.click()
        elif n == "8":
            boton = driver.find_element_by_id(pantallaPrincipal["btn_numerico_ocho"]["value_id"])
            boton.click()
        elif n == "9":
            boton = driver.find_element_by_id(pantallaPrincipal["btn_numerico_nueve"]["value_id"])
            boton.click()

def pago(tipoDeCompra):
    if tipoDeCompra == "tarjeta":
        boton = driver.find_element_by_xpath(pantallaPrincipal["btn_cobrar"]["value_xpath"])
        boton.click()
        return True
    elif tipoDeCompra == "qr":
        boton = driver.find_element_by_id(pantallaPrincipal["btn_generar_qr"]["value_id"])
        boton.click()
        return True
    elif tipoDeCompra == "dividido":
        boton = driver.find_element_by_id(pantallaPrincipal["btn_pago_dividido"]["value_id"])
        boton.click()
        return True

def cantidad_de_cuotas(tipoDeCompra, cuotasDeseadas):
    if tipoDeCompra == "tarjeta":
        if cuotasDeseadas == "1":
            boton = driver.find_element_by_id(pantallaCuotas["btn_aceptar"]["value_id"])
            boton.click()
        elif cuotasDeseadas == "3":
            boton = driver.find_element_by_id(pantallaCuotas["btn_tres_cuotas"]["value_id"])
            boton.click()
            boton = driver.find_element_by_id(pantallaCuotas["btn_aceptar"]["value_id"])
            boton.click()
        elif cuotasDeseadas == "6":
            boton = driver.find_element_by_id(pantallaCuotas["btn_seis_cuotas"]["value_id"])
            boton.click()
            boton = driver.find_element_by_id(pantallaCuotas["btn_aceptar"]["value_id"])
            boton.click()
        elif cuotasDeseadas == "12":
            boton = driver.find_element_by_id(pantallaCuotas["btn_doce_cuotas"]["value_id"])
            boton.click()
            boton = driver.find_element_by_id(pantallaCuotas["btn_aceptar"]["value_id"])
            boton.click()
        else:
            cuotas_manual = driver.find_element_by_id(pantallaCuotas["btn_ingresar_cuotas"]["value_id"])
            cuotas_manual.send_keys(cuotasDeseadas)
            boton = driver.find_element_by_id(pantallaCuotas["btn_aceptar"]["value_id"])
            boton.click()

    elif tipoDeCompra == "qr":
        if cuotasDeseadas == "1":
                boton = driver.find_element_by_id(pantallaCuotas["btn_aceptar"]["value_id_qr"])
                boton.click()
        elif cuotasDeseadas == "3":
                boton = driver.find_element_by_id(pantallaCuotas["btn_tres_cuotas"]["value_id_qr"])
                boton.click()
                boton = driver.find_element_by_id(pantallaCuotas["btn_aceptar"]["value_id_qr"])
                boton.click()
        elif cuotasDeseadas == "6":
                boton = driver.find_element_by_id(pantallaCuotas["btn_seis_cuotas"]["value_id_qr"])
                boton.click()
                boton = driver.find_element_by_id(pantallaCuotas["btn_aceptar"]["value_id_qr"])
                boton.click()
        elif cuotasDeseadas == "12":
                boton = driver.find_element_by_id(pantallaCuotas["btn_doce_cuotas"]["value_id_qr"])
                boton.click()
                boton = driver.find_element_by_id(pantallaCuotas["btn_aceptar"]["value_id_qr"])
                boton.click()
        else:
            cuotas_manual = driver.find_element_by_id(pantallaCuotas["btn_ingresar_cuotas"]["value_id_qr"])
            cuotas_manual.send_keys(cuotasDeseadas)

def imprimir_ticket_cliente():
    btn_impresion = driver.find_element_by_id(pantallaTicket["btn_imprimir_ticket"]["value_id"])
    btn_impresion.click()

def continuar():
    btn_continuar = driver.find_element_by_id(pantallaTicket["btn_continuar"]["value_id"])
    btn_continuar.click()

def terminar():
    btn_terminar = driver.find_element_by_id(pantallaTicket["btn_terminar"]["value_id"])
    btn_terminar.click()

def VerificarPantalla(deseada):
    actual = driver.current_activity()
    bandera = "incorrecto"
    if deseada == actual:
        bandera = "correcto"
        return bandera
    else:
        return bandera

class TestDeTerminal(unittest.TestCase):

    def setUp(self):
        print("Iniciando Pruebas")

    def test_pago_qr(self):
        ingresar_monto("1000")
        pago("qr")
        time.sleep(2)#cambiar este paso por una comprobacion de la pantalla de cuotas
        cantidad_de_cuotas("qr", "12")
        time.sleep(35)#agregar comprobacion de mensaje transaccion aprobada
        imprimir_ticket_cliente()
        time.sleep(5)#comprobar la impresion del ticket
        continuar()
        time.sleep(5)#comprobar la pantalla de ticket comercio
        terminar()

    def tearDown(self):
        print("finalizado")


if __name__ == '__main__':
    unittest.main()