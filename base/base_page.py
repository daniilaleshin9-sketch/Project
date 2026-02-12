import allure
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from metaclasses.meta_locator import MetaLocator

class BasePage(metaclass=MetaLocator):

    LOGO = ("xpath", "//*[text() = 'Logo']")

    def __init__(self, driver):
        self.driver: WebDriver = driver

    def open(self):
        with allure.step(f"Открываем {self._PAGE_URL} page"):
            self.driver.get(self._PAGE_URL)

    def wait_element_value(self, locator, value, timeout=10):
        """Ждет пока в поле ввода появится указанный текст"""
        return WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element_value(locator, value)
        )
    def wait_element_visible(self, locator, timeout=10):
        """Явное ожидание видимости элемента"""
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_element_clickable(self, locator, timeout=10):
        """Явное ожидание кликабельности элемента"""
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def wait_page_loaded(self, timeout=10):
        """Ожидание полной загрузки страницы по появлению логотипа"""
        self.wait_element_visible(self.LOGO, timeout)
        return self


    def wait_element_text(self, locator, text, timeout=10):
        """Явное ожидание текста в элементе"""
        return WebDriverWait(self.driver, timeout).until(
            EC.text_to_be_present_in_element(locator, text)
        )