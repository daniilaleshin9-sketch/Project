import allure
from base.base_page import BasePage

class MainPage(BasePage):
    _PAGE_URL = 'http://2.59.41.2:6700/'
    _PROFILE_BUTTON = '//*[@class="Header_link__k8Ywf"][text() = "Профиль"]'

    @allure.step("Нажимаем кнопку профиль")
    def click_profile_button(self):
        self.driver.find_element(*self._PROFILE_BUTTON).click()