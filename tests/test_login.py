from pages.login_page import LoginPage
from config import (
    BASE_URL,
    MAIL_LOGIN_USER,
    PASSWORD_USER,
    WRONG_MAIL_LOGIN_USER,
    WRONG_PASSWORD
)

def test_open_site(driver):
    """Открытие страницы"""
    page = LoginPage(driver)
    page.open()

    assert BASE_URL in driver.current_url

def test_successful_login(driver):
    """Успешная авторизация"""
    page = LoginPage(driver)
    page.open()
    page.login_success(MAIL_LOGIN_USER, PASSWORD_USER)

    assert "lamoda.by" in driver.current_url
    assert page.is_profile_page_opened()

def test_login_wrong_mail(driver):
    """Авторизация с неверным email"""
    page = LoginPage(driver)
    page.open()
    page.login_fail(WRONG_MAIL_LOGIN_USER, PASSWORD_USER)

    assert "Неверный логин или пароль" in page.get_error_text()

def test_login_wrong_password(driver):
    """Авторизация с неверным паролем"""
    page = LoginPage(driver)
    page.open()
    page.login_fail(MAIL_LOGIN_USER, WRONG_PASSWORD)

    assert "Неверный логин или пароль" in page.get_error_text()
