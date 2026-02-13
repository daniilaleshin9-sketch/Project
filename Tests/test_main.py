import allure
import pytest
import time
from base.base_test import BaseTest


class TestMain(BaseTest):

    @allure.step("Создаём задачу")
    def test_add_task(self, auth_driver):
        self.main_page.add_name_task()
        self.main_page.add_description_task()
        self.main_page.add_date_task()
        self.main_page.add_time_task()
        self.main_page.click_submit_button_task()

    @allure.step("Редактируем задачу")
    def test_edit_task(self, auth_driver):
        self.main_page.edit_task_title()
        self.main_page.edit_description()
        self.main_page.edit_date_task()
        self.main_page.edit_time_task()
        self.main_page.check_edit_title()
        self.main_page.check_edit_description()
        self.main_page.check_edit_date()
        self.main_page.check_edit_date()


