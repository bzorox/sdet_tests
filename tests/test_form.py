import pytest
from selenium import webdriver
from pages.form_page import FormPage

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

def test_form_positive(driver):
    page = FormPage(driver)
    page.open()

    page.fill_name("John")
    page.fill_password("1234")
    page.select_drinks()
    page.select_color()
    page.select_automation()
    page.fill_email("name@example.com")
    page.fill_message()

    page.submit()
    assert "Message received!" in page.get_alert_text()

def test_form_negative(driver):
    page = FormPage(driver)
    page.open()

    page.fill_name("John")
    page.submit()

    try:
        alert_text = page.get_alert_text()
        assert False, "Alert should not appear"
    except:
        assert True
