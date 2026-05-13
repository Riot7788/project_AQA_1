from selenium.webdriver.common.by import By
from config import BASE_URL, MEN_HOME_URL
from pages.base_page import BasePage


class MenPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver, BASE_URL)

    def open_men_home_page(self):
        self.driver.get(MEN_HOME_URL)

