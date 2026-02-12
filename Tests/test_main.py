import allure
import pytest
import time
from base.base_test import BaseTest

class TestMain(BaseTest):

    @allure.step("Заполняем поля задачи")
    def test_add_param_task(self, auth_driver):
        self.main_page.add_name_task()
        self.main_page.add_description_task()
        self.main_page.add_date_task()
        self.main_page.add_time_task()
        self.main_page.click_submit_button_task()


