from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome(executable_path="C:/Users/jagutierrez/Documents/GitHub/AutomatizacionTerminales/AutomatizacionTerminalesAndroid/drivers/chromedriver.exe")
driver.get("https://prisma.paystore.me/#!/login")
driver.maximize_window()
time.sleep(5)

username = driver.find_element(By.ID, "input_0")
password = driver.find_element(By.ID, "input_1")
username.send_keys("jagutierrez")
time.sleep(3)
password.send_keys("JavierAntonio")
time.sleep(3)
driver.find_element(By.XPATH, "/html/body/div[2]/div/md-content/ui-view/div/div/md-card/ph-form/ng-form/div[2]/div[2]/button/div[1]").click()


