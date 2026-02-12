from utiles.generators import Generator
from datetime import datetime
from base.base_page import BasePage
import time
import allure
generator = Generator()

class MainPage(BasePage):
    _PAGE_URL = 'http://2.59.41.2:6700/'
    _PROFILE_BUTTON = '//*[@class="Header_link__k8Ywf"][text() = "Профиль"]'
    _title = '//*[@name="title"]'
    _description = '//*[@placeholder="Описание задачи"]'
    _button_date = '//*[@id="date-input-create"]'
    _button_time = '//*[@id="time-input-create-how"]'
    _submit_button_task = '//*[@type="submit"]'
    _submit_task_created = '//*[@class="Success_ok__y8HHg"]'
    _list_tasks = '//*[@class="mt-2.5"]'
    _task_title = '//*[@class="mt-2.5"]//h4[@class="TodoItem_content__J_7bo"]'


    def __init__(self, driver):
        super().__init__(driver)
        self.generator = Generator()
        self.created_task_name = None

    @allure.step("Нажимаем кнопку профиль")
    def click_profile_button(self):
        self.driver.find_element(*self._PROFILE_BUTTON).click()

    @allure.step("Вводим имя для задачи")
    def add_name_task(self):
        name_task = self.generator.generate_string()
        self.wait_page_loaded()
        self.wait_element_clickable(self._title)
        self.driver.find_element(*self._title).send_keys(name_task)
        self.created_task_name = name_task

    @allure.step("Вводим описание задачи")
    def add_description_task(self):
        description_task = self.generator.generate_string()
        self.wait_page_loaded()
        self.wait_element_clickable(self._description)
        self.driver.find_element(*self._description).send_keys(description_task)

    @allure.step("Вводим дату задачи")
    def add_date_task(self):
        current_date = self.generator.get_current_date()
        date_field = self.wait_element_clickable(self._button_date)
        date_field.send_keys(current_date)

    @allure.step("Вводим точное время")
    def add_time_task(self):
        current_time = self.generator.get_current_time()
        time_field = self.wait_element_clickable(self._button_time)
        time_field.send_keys(current_time)

    @allure.step("Добавляем задачу")
    def click_submit_button_task(self):
        self.driver.find_element(*self._submit_button_task).click()
        self.wait_element_clickable(self._submit_task_created)
        self.driver.find_element(*self._submit_task_created).click()
        time.sleep(0.5)
        all_tasks = self.driver.find_elements(*self._task_title)
        tasks_text = [task.text for task in all_tasks]
        assert self.created_task_name in str(tasks_text), f"Задача '{self.created_task_name}' не найдена!"