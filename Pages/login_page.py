import allure
from base.base_page import BasePage


class LoginPage(BasePage):
    _PAGE_URL = 'http://2.59.41.2:6700/auth/login'
    _LOGIN_FIELD = '//*[@type="email"]'
    _PASSWORD_FIELD = '//*[@id="login-pass"]'
    _BUTTON_LOGIN = '//*[@type="submit"][text() = "Войти"]'

    @allure.step("Вводим логин")
    def login(self, login):
        self.driver.find_element(*self._LOGIN_FIELD).send_keys(login)

    @allure.step("Вводим пароль")
    def password(self, password):
        self.driver.find_element(*self._PASSWORD_FIELD).send_keys(password)

    @allure.step("Нажимаем кнопку авторизации")
    def button_login(self):
        self.driver.find_element(*self._BUTTON_LOGIN).click()
