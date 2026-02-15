from selenium.webdriver.common.by import By

from utiles.generators import Generator
from datetime import datetime
from base.base_page import BasePage
from selenium.webdriver.remote.webelement import WebElement
import time
import allure
generator = Generator()

class MainPage(BasePage):
    _PAGE_URL = 'http://2.59.41.2:6700/'
    _PROFILE_BUTTON = '//*[@class="Header_link__k8Ywf"][text() = "Профиль"]'
    _title = '//*[@name="title"]'
    _description = '//*[@placeholder="Описание задачи"]'
    _button_date = '//*[@id="date-input-create"]'
    _button_date_edit = '//*[@id="date-input-edit"]'
    _button_time = '//*[@id="time-input-create-how"]'
    _button_time_edit = '//*[@id="time-input-edit"]'
    _submit_button_task = '//*[@type="submit"]'
    _submit_button_edit_task = '//*[@class="EditTodo_button__ySCIK"][@type="submit"]'
    _edit_task = '//*[@id="edit-module"]//*[text() = "Изменить"]'
    _edited_task = '//*[@class="Success_ok__y8HHg"][text() = "ОК"]'
    _open_task = '//li[1]/ul/div/h4'
    _view_title_task = '//h1[@class="Review_title__AHmpO"]'
    _view_description_task = '//ul/div[1]//textarea'
    _view_date_task = '//div[3]//div[1]/label[1]/input'
    _view_time_task = '//div[3]//div[1]/label[2]/input'
    _submit_task_created = '//*[@class="Success_ok__y8HHg"]'
    _list_tasks = '//*[@class="mt-2.5"]'
    _task_title = '//*[@class="mt-2.5"]//h4[@class="TodoItem_content__J_7bo"]'
    _first_task_title_edit = '//li[1]//button[1]/img'
    _opened_task = '//*[@class="EditTodo_wrapper___1B6a"]'
    _value_name = '//*[@id="edit-module"]//*[@placeholder="Заголовок"]'
    _value_description = '//*[@id="edit-module"]//*[@placeholder="Описание задачи"]'
    _completed_task = '//li[1]/ul/div[1]//*[@class="TodoItem_checkmark__gytmH"]'
    _completed_task_true = '//*[text() = "Завершить"]'
    _completed_task_true_end = '//*[@class="Success_ok__y8HHg"]'
    _completed_task_true_assert = '//li[1]/ul/div[1]/div[1]/div/span'


    def __init__(self, driver):
        super().__init__(driver)
        self.generator = Generator()
        self.created_task_name = None
        self.edit_title_value = None
        self.edit_description_value = None
        self.current_date_edit = None
        self.current_time_edit = None

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
        time.sleep(5)

    @allure.step("Добавляем задачу")
    def click_submit_button_task(self):
        self.driver.find_element(*self._submit_button_task).click()
        self.wait_element_clickable(self._submit_task_created)
        self.driver.find_element(*self._submit_task_created).click()
        time.sleep(2)
        all_tasks = self.driver.find_elements(*self._task_title)
        tasks_text = [task.text for task in all_tasks]
        assert self.created_task_name in str(tasks_text), f"Задача '{self.created_task_name}' не найдена!"

    @allure.step("Редактируем задачу")
    def edit_task_title(self):
        self.wait_page_loaded()
        self.wait_element_clickable(self._first_task_title_edit)
        self.driver.find_element(*self._first_task_title_edit).click()
        self.wait_element_clickable(self._opened_task)
        title_field = self.driver.find_element(*self._value_name)
        title_field.clear()
        self.edit_title_value = self.generator.generate_string()
        title_field.send_keys(self.edit_title_value)
        self.edit_title_value = self.edit_title_value

    @allure.step("Редактируем описание")
    def edit_description(self):
        description_field = self.driver.find_element(*self._value_description)
        description_field.clear()
        self.edit_description_value = self.generator.generate_string()
        description_field.send_keys(self.edit_description_value)
        self.edit_description_value = self.edit_description_value

    @allure.step("Редактируем дату задачи")
    def edit_date_task(self):
        current_date_edit = self.generator.get_current_date()
        date_field_edit = self.wait_element_clickable(self._button_date_edit)
        date_field_edit.send_keys(current_date_edit)
        self.current_date_edit = current_date_edit

    @allure.step("Редактируем время задачи")
    def edit_time_task(self):
        current_time_edit = self.generator.get_current_time()
        time_field_edit = self.wait_element_clickable(self._button_time_edit)
        time_field_edit.send_keys(current_time_edit)
        self.current_time_edit = current_time_edit
        self.driver.find_element(*self._submit_button_edit_task).click()
        self.wait_element_clickable(self._edit_task)
        self.driver.find_element(*self._edit_task).click()
        self.wait_element_clickable(self._edited_task)
        self.driver.find_element(*self._edited_task).click()

    @allure.step("Проверяем отредактированный заголовок")
    def check_edit_title(self):
        task_xpath = f'//*[text()="{self.edit_title_value}"]'
        task_element = self.wait_element_clickable((By.XPATH, task_xpath), timeout=5)
        task_element.click()
        self.wait_element_visible(self._view_title_task)
        view_title = self.driver.find_element(*self._view_title_task).text
        assert self.edit_title_value == view_title

    @allure.step("Проверяем отредактированный заголовок")
    def check_edit_description(self):
        self.wait_element_visible(self._view_description_task)
        view_description = self.driver.find_element(*self._view_description_task).get_attribute("placeholder")
        assert self.edit_description_value == view_description, \
            f"Ожидали '{self.edit_description_value}', получили '{view_description}'"

    @allure.step("Проверяем отредактированную дату")
    def check_edit_date(self):
        _view_date_task = self.driver.find_element(*self._view_date_task).get_attribute("placeholder")
        day, month, year = self.current_date_edit.split('.')
        expected_format = f"{year}-{month}-{day}"
        assert expected_format == _view_date_task, \
            f"Ожидали '{expected_format}', получили '{_view_date_task}'"

    @allure.step("Проверяем отредактированную дату")
    def check_edit_time(self):
        _view_time_task = self.driver.find_element(*self._view_time_task).get_attribute("placeholder")
        assert self.current_time_edit == _view_time_task, \
            f"Ожидали '{self.current_time_edit}', получили '{_view_time_task}'"

    @allure.step("Выполняем задачу")
    def complete_task(self):
        self.wait_element_clickable(self._completed_task, 2)
        time.sleep(1)
        self.driver.find_element(*self._completed_task).click()
        time.sleep(1)
        self.wait_element_clickable(self._completed_task_true, 2)
        time.sleep(1)
        self.driver.find_element(*self._completed_task_true).click()
        time.sleep(1)
        self.wait_element_clickable(self._completed_task_true_end, 2)
        time.sleep(1)
        self.driver.find_element(*self._completed_task_true_end).click()
        time.sleep(1)
        native_checkbox = self.driver.find_element(*self._completed_task_true_assert)
        # time.sleep(1)
        # assert native_checkbox.is_selected() is True



