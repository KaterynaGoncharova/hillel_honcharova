from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()

driver.get("http://localhost:8000/dz.html")

frame1 = WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.ID, "frame1")))

input1 = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "input2")))
input1.send_keys("Frame1_Secret")
button1 = driver.find_element(By.XPATH, "//button[text()='Перевірити']")
button1.click()

time.sleep(1)
alert1 = Alert(driver)
alert1_text1 = alert1.text
print("Текст для першого фрейму:", alert1_text1)

if alert1_text1 == "Верифікація пройшла успішно!":
    print("Перевірка для фрейму 1 успішна!")
else:
    print("Помилка в фреймі 1!")

alert1.accept()

driver.switch_to.default_content()
frame2 = WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.ID, "frame2")))

input2 = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.ID, "input1")))
input2.send_keys("Frame2_Secret")
button2 = driver.find_element(By.XPATH, "//button[text()='Перевірити']")
button2.click()

time.sleep(1)
alert2 = Alert(driver)
alert2_text2 = alert2.text
print("Текст для другого фрейму:", alert2_text2)

if alert2_text2 == "Верифікація пройшла успішно!":
    print("Перевірка для фрейму 2 успішна!")
else:
    print("Помилка в фреймі 2!")

alert2.accept()

driver.quit()