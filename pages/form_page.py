from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains

class FormPage:
    URL = "https://practice-automation.com/form-fields/"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.actions = ActionChains(driver)

    def open(self):
        self.driver.get(self.URL)
        self.wait.until(EC.presence_of_element_located((By.ID, "feedbackForm")))
        # Закрываем возможные попапы
        self._close_popups()

    def _close_popups(self):
        """Закрывает всплывающие окна, если есть"""
        try:
            # Пробуем закрыть куки-баннер или другие попапы
            close_buttons = self.driver.find_elements(By.XPATH, "//button[contains(text(), 'Close')] | //button[contains(text(), '×')] | //button[contains(@class, 'close')]")
            for btn in close_buttons:
                if btn.is_displayed():
                    btn.click()
        except:
            pass

    def _scroll_to_element(self, element):
        """Прокручивает страницу до элемента"""
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        time.sleep(0.5)

    def fill_name(self, name):
        element = self.wait.until(EC.presence_of_element_located((By.ID, "name-input")))
        self._scroll_to_element(element)
        element.clear()
        element.send_keys(name)

    def fill_password(self, password):
        element = self.driver.find_element(By.CSS_SELECTOR, "input[type='password']")
        self._scroll_to_element(element)
        element.clear()
        element.send_keys(password)

    def select_drinks(self):
        milk = self.wait.until(EC.element_to_be_clickable((By.ID, "drink1")))
        self._scroll_to_element(milk)
        milk.click()
        
        coffee = self.wait.until(EC.element_to_be_clickable((By.ID, "drink2")))
        self._scroll_to_element(coffee)
        coffee.click()

    def select_color(self):
        color = self.wait.until(EC.element_to_be_clickable((By.ID, "color4")))
        self._scroll_to_element(color)
        # Используем JavaScript для клика, если обычный не работает
        try:
            color.click()
        except:
            self.driver.execute_script("arguments[0].click();", color)

    def select_automation(self):
        dropdown = self.wait.until(EC.element_to_be_clickable((By.ID, "automation")))
        self._scroll_to_element(dropdown)
        select = Select(dropdown)
        select.select_by_value("yes")

    def fill_email(self, email):
        element = self.driver.find_element(By.ID, "email")
        self._scroll_to_element(element)
        element.clear()
        element.send_keys(email)

    def fill_message(self):
        message = "4 Selenium WebDriver"
        element = self.driver.find_element(By.ID, "message")
        self._scroll_to_element(element)
        element.clear()
        element.send_keys(message)

    def submit(self):
        button = self.wait.until(EC.element_to_be_clickable((By.ID, "submit-btn")))
        self._scroll_to_element(button)
        try:
            button.click()
        except:
            self.driver.execute_script("arguments[0].click();", button)

    def get_alert_text(self):
        alert = self.wait.until(EC.alert_is_present())
        text = alert.text
        alert.accept()
        return text

import time  # добавить в начало файла
