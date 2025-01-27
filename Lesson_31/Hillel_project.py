from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest

class NovaPoshtaTracker:
    def __init__(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.implicitly_wait(10)

    def get_status(self, parcel_number):

        self.driver.get("https://novaposhta.ua/tracking")
        search_input = self.driver.find_element(By.ID, "en")
        search_input.send_keys(parcel_number)

        search_button = self.driver.find_element(By.CSS_SELECTOR, ".track__form-group-btn.green-active")
        search_button.click()

        ok_button = self.driver.find_element(By.XPATH, "//button/span[contains(text(), 'Добре')]")
        ok_button.click()

        try:
            status_element = WebDriverWait(self.driver, 20).until(
                EC.presence_of_element_located((By.CLASS_NAME, "header__status-text"))
            )
            return status_element.text
        except:
            print("Статус не знайдено або елемент не з'явився вчасно.")
            return None

    def close(self):
        self.driver.quit()

@pytest.mark.parametrize(
    "parcel_number, expected_status",
    [
        ("20451080897440", "Отримана"),
    ],
)
def test_parcel_status(parcel_number, expected_status):
    tracker = NovaPoshtaTracker()
    try:
        status = tracker.get_status(parcel_number)
        assert status == expected_status, f"Очікуваний статус: {expected_status}, отриманий статус: {status}"
    finally:
        tracker.close()
