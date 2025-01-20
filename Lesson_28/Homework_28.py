import pytest
from selenium import webdriver
from signup_page import SignUpPage


@pytest.fixture
def driver():
    driver = webdriver.Chrome()

    driver.get("https://guest:welcome2qauto@qauto2.forstudy.space")

    yield driver
    driver.quit()


def test_user_registration(driver):
    signup_page = SignUpPage(driver)

    signup_page.click_sign_up_button()

    signup_page.fill_registration_form("Kateryna", "Honcharova", "kgoncharova14@gmail.com", "Qwerty1234")

    signup_page.click_register_button()

    assert signup_page.is_registration_successful()

    print("Реєстрація успішно завершена!")