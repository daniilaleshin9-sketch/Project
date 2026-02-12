from selenium.webdriver.support import expected_conditions as EC
import allure
from selenium.webdriver.support.wait import WebDriverWait

from base.base_page import BasePage


class LoginPage(BasePage):
    _PAGE_URL = 'http://2.59.41.2:6700/auth/login'
    _LOGIN_FIELD = '//*[@type="email"]'
    _PASSWORD_FIELD = '//*[@id="login-pass"]'
    _BUTTON_LOGIN = '//*[@type="submit"][text() = "Войти"]'


    @allure.step("Вводим логин")
    def login(self, login):
        self.wait_element_clickable(self._LOGIN_FIELD)
        self.driver.find_element(*self._LOGIN_FIELD).send_keys(login)
        self.wait_element_value(self._LOGIN_FIELD, login)
    @allure.step("Вводим пароль")
    def password(self, password):
        self.wait_element_clickable(self._PASSWORD_FIELD)
        self.driver.find_element(*self._PASSWORD_FIELD).send_keys(password)
        self.wait_element_value(self._PASSWORD_FIELD, password)

    @allure.step("Нажимаем кнопку авторизации")
    def button_login(self):
        self.driver.find_element(*self._BUTTON_LOGIN).click()



