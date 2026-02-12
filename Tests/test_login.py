import allure
import pytest
import time
from base.base_test import BaseTest
from Data.Credentials import Credentials

@pytest.mark.usefixtures("driver")
class TestLogin(BaseTest):

    @pytest.mark.smoke
    @allure.story("Авториация в аккаунт")
    def test_login(self):
        self.login_page.open()
        self.login_page.login(Credentials.LOGIN)
        self.login_page.password(Credentials.PASSWORD)
        self.login_page.button_login()
