from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from config import BASE_URL


class LoginPage(BasePage):
    LOGIN_BUTTON = (By.XPATH, '//button[normalize-space()="Войти"]')
    LOGIN_USER_INPUT = (By.CSS_SELECTOR, "input[aria-label='Электронная почта']")
    INPUT_LOGIN_BUTTON = (By.XPATH, "//button[@type='submit' and normalize-space()='Войти']")
    PASSWORD_USER_INPUT = (By.CSS_SELECTOR, "input[type='password']")
    INPUT_LOGIN_BUTTON_PASSWORD = (By.XPATH, "//button[@type='submit' and normalize-space()='Войти']")
    PROFILE_PAGE = (By.CSS_SELECTOR, "a[href='/sales/order/history/']")

    def __init__(self, driver):
        super().__init__(driver, BASE_URL)

    def login(self, username, password):
        self.click(self.LOGIN_BUTTON)

        self.type(self.LOGIN_USER_INPUT, username)
        self.click(self.INPUT_LOGIN_BUTTON)

        self.find(self.PASSWORD_USER_INPUT)

        self.type(self.PASSWORD_USER_INPUT, password)
        self.click(self.INPUT_LOGIN_BUTTON_PASSWORD)

        self.find(self.PROFILE_PAGE)


    def is_profile_page_opened(self):
        return self.find(self.PROFILE_PAGE).is_displayed()


