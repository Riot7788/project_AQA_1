from pages.login_page import LoginPage
from config import (
    BASE_URL,
    MAIL_LOGIN_USER,
    PASSWORD_USER
)

def test_open_site(driver):
    page = LoginPage(driver)
    page.open()

    assert BASE_URL in driver.current_url

def test_successful_login(driver):
    page = LoginPage(driver)
    page.open()
    page.login(MAIL_LOGIN_USER, PASSWORD_USER)

    assert "lamoda.by" in driver.current_url
    assert page.is_profile_page_opened()
