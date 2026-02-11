import allure
from selenium.webdriver.ie.webdriver import WebDriver
from metaclasses.meta_locator import MetaLocator

class BasePage(metaclass=MetaLocator):

    _LOGO = ("xpath", "//*[text() = 'Logo']")

    def __init__(self, driver):
        self.driver: WebDriver = driver

    def open(self):
        with allure.step(f"Открываем {self._PAGE_URL} page"):
            self.driver.get(self._PAGE_URL)