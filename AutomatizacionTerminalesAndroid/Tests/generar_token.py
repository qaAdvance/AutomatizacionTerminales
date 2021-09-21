from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="C:/Users/jagutierrez/Documents/GitHub/AutomatizacionTerminales/AutomatizacionTerminalesAndroid/drivers/chromedriver.exe")
driver.get("https://prisma.paystore.me/#!/login")
driver.maximize_window()
time.sleep(5)

usuario = "jagutierrez"
contrasena = "JavierAntonio"
comercio = "000404"
terminal = "38010303"
tiempo_entre_pasos = 2

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
time.sleep(10)
'''Filtrado en la pestaña comercios del adquirente'''
driver.find_element(By.XPATH, "body > app-root > li-theme-container > app-merchant-maintenance > ph-table-maintenance > div > mat-card-title > div.ngx-ph-actions > button:nth-child(1)").click()
time.sleep(4)
driver.find_element(By.XPATH, "//*[@id='select_69']").click()
time.sleep(tiempo_entre_pasos)
driver.find_element(By.XPATH, "//*[@id='select_option_81']/div").click()
time.sleep(tiempo_entre_pasos)
driver.find_element(By.CSS_SELECTOR, "#input_113").click()
time.sleep(tiempo_entre_pasos)
driver.find_element(By.CSS_SELECTOR, "#input_113").send_keys(comercio)
time.sleep(tiempo_entre_pasos)
driver.find_element(By.XPATH, "//*[@id='painel-filter-container-parent']/div[2]/md-card/ph-filter-form/ph-form/ng-form/div/div[1]/button/ng-md-icon").click()
time.sleep(tiempo_entre_pasos)
driver.find_element(By.XPATH, "//*[@id='painel-filter-container-parent']/div[2]/md-card/ph-filter-form/ph-form/ng-form/div/div[3]/button[3]").click()
time.sleep(tiempo_entre_pasos)
driver.find_element(By.XPATH, "//*[@id='app-content']/ui-view/ui-view/div/ph-crud-maintenance/div/md-card/div[2]/ph-data-table/md-table-container/table/tbody/tr/td[1]").click()
time.sleep(tiempo_entre_pasos)
driver.find_element(By.XPATH, "//*[@id='app-content']/ui-view/ui-view/div/ph-crud-maintenance/div/md-card/div[1]/div[1]/button[9]/ng-md-icon").click()
time.sleep(tiempo_entre_pasos)
driver.find_element(By.CSS_SELECTOR, "#painel-filter-container-parent > button > ng-md-icon").click()
time.sleep(tiempo_entre_pasos)
'''Filtrado en la pestaña terminales logicos del adquirente'''
driver.find_element(By.CSS_SELECTOR, "#select_165").click()
time.sleep(tiempo_entre_pasos)
driver.find_element(By.CSS_SELECTOR, "#select_option_170").click()
time.sleep(tiempo_entre_pasos)
driver.find_element(By.CSS_SELECTOR, "#input_199").click()
time.sleep(tiempo_entre_pasos)
driver.find_element(By.CSS_SELECTOR, "#input_199").send_keys(terminal)
time.sleep(tiempo_entre_pasos)
driver.find_element(By.XPATH, "//*[@id='painel-filter-container-parent']/div[2]/md-card/ph-filter-form/ph-form/ng-form/div/div[1]/button").click()
time.sleep(tiempo_entre_pasos)
driver.find_element(By.XPATH, "//*[@id='painel-filter-container-parent']/div[2]/md-card/ph-filter-form/ph-form/ng-form/div/div[3]/button[3]").click()
time.sleep(tiempo_entre_pasos)
'''Click en la terminal filtrada y en el icono de token'''
driver.find_element(By.XPATH, "//*[@id='app-content']/ui-view/ui-view/div/ph-crud-maintenance/div/md-card/div[2]/ph-data-table/md-table-container/table/tbody/tr/td[1]").click()
time.sleep(tiempo_entre_pasos)
driver.find_element(By.CSS_SELECTOR, "#app-content > ui-view > ui-view > div > ph-crud-maintenance > div > md-card > div.maintenance-buttons.layout-gt-xs-row.layout-column > div.layout-wrap.layout-row.layout-align-start-start > button:nth-child(10)").click()
time.sleep(tiempo_entre_pasos)
token = driver.find_element(By.CSS_SELECTOR, "#token").get_attribute('value')
print(token)
time.sleep(10)
driver.close()
driver.quit()
