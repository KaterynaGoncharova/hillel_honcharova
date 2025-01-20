from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class SignUpPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://qauto2.forstudy.space"

    def open(self):
        self.driver.get(self.url)

    def click_sign_up_button(self):
        sign_up_button = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[contains(text(), 'Sign up')]"))
        )
        sign_up_button.click()

    def fill_registration_form(self, name, last_name, email, password):
        self.driver.find_element(By.ID, "signupName").send_keys(name)
        self.driver.find_element(By.ID, "signupLastName").send_keys(last_name)
        self.driver.find_element(By.ID, "signupEmail").send_keys(email)
        self.driver.find_element(By.ID, "signupPassword").send_keys(password)
        self.driver.find_element(By.ID, "signupRepeatPassword").send_keys(password)

    def click_register_button(self):
        register_button = self.driver.find_element(By.XPATH, "//button[text()='Register']")
        register_button.click()

    def is_registration_successful(self):
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//button[text()='Sign In']"))
        )
        return True