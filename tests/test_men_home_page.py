from pages.men_home_page import MenPage


def test_open_men_home_page(driver):
    """Открытие страницы для мужчин"""
    page = MenPage(driver)
    page.open_men_home_page()

    assert "men-home" in driver.current_url

