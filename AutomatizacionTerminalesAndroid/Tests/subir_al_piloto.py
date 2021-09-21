from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="C:/Users/jagutierrez/Documents/GitHub/AutomatizacionTerminales/AutomatizacionTerminalesAndroid/drivers/chromedriver.exe")
driver.get("https://prisma.paystore.me/#!/login")
driver.maximize_window()
time.sleep(5)


def filtrado_por_codigo_de_version_igual_a(version_a_filtrar):
    time.sleep(tiempo_entre_pasos)
    driver.find_element(By.CSS_SELECTOR, "#painel-filter-container-parent > button").click()
    time.sleep(tiempo_entre_pasos)
    driver.find_element(By.CSS_SELECTOR, "#select_155").click()
    time.sleep(tiempo_entre_pasos)
    driver.find_element(By.CSS_SELECTOR, "#select_option_159 > div.md-text.ng-binding").click()
    time.sleep(tiempo_entre_pasos)
    driver.find_element(By.CSS_SELECTOR, "#input_181").send_keys(version_a_filtrar)
    time.sleep(tiempo_entre_pasos)
    driver.find_element(By.CSS_SELECTOR,
                        "#painel-filter-container-parent > div.filter-select-container > md-card > ph-filter-form > ph-form > ng-form > div > div.filter-select-inner-container.ng-scope.layout-align-start-start.layout-row > button > ng-md-icon").click()
    time.sleep(tiempo_entre_pasos)
    driver.find_element(By.CSS_SELECTOR,
                        "#painel-filter-container-parent > div.filter-select-container > md-card > ph-filter-form > ph-form > ng-form > div > div.ng-scope.layout-align-end-end.layout-row > button.md-raised.ph-filter-submit-button.md-primary.md-button.md-PEDRO____IVO_content-theme.md-ink-ripple").click()


usuario = "jagutierrez"
contrasena = "JavierAntonio"
comercio = "000393"
terminal = "38010303"
tiempo_entre_pasos = 3
codigo_de_version_1 = "104"

'''Login y inicialiacion en el adquirente'''
username = driver.find_element(By.ID, "input_0")
password = driver.find_element(By.ID, "input_1")
username.send_keys(usuario)
time.sleep(tiempo_entre_pasos)
password.send_keys(contrasena)
time.sleep(tiempo_entre_pasos)
driver.find_element(By.XPATH, "/html/body/div[2]/div/md-content/ui-view/div/div/md-card/ph-form/ng-form/div[2]/div[2]/button/div[1]").click()
time.sleep(tiempo_entre_pasos)
driver.find_element(By.XPATH, "//*[@id='app-content']/ui-view/ui-view/ph-crud-maintenance/div/md-card/div[2]/ph-data-table/md-table-container/table/tbody/tr[4]/td[2]/div").click()
time.sleep(tiempo_entre_pasos)
driver.find_element(By.XPATH, "//*[@id='app-content']/ui-view/ui-view/ph-crud-maintenance/div/md-card/div[1]/div[1]/button[8]/ng-md-icon").click()
time.sleep(tiempo_entre_pasos)
driver.switch_to.window(driver.window_handles[1])
'''Click en la pestaña de Applicaciones'''
time.sleep(tiempo_entre_pasos)
driver.find_element(By.CSS_SELECTOR, "#ph-navigation > div:nth-child(10) > button > div.ng-scope.layout-align-start-center.layout-row > span").click()
'''Click en la pestaña de en piloto'''
time.sleep(tiempo_entre_pasos)
driver.find_element(By.CSS_SELECTOR, "#ph-navigation > div:nth-child(10) > div > div:nth-child(2) > button > div > span").click()
'''Click en filtro codigo de version de piloto'''
filtrado_por_codigo_de_version_igual_a(codigo_de_version_1)
'''Hacer click en la primera opcion y entrar a la opcion agregar app al piloto'''
time.sleep(10)
driver.close()
driver.quit()
