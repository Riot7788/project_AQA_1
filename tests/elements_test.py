from pages.base_page import BasePage
from selenium.webdriver.common.by import By


BASE_URL = 'https://www.lamoda.by/'

def test_open_site(driver):
    page = BasePage(driver, BASE_URL)
    page.open()
