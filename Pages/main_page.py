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
    _button_date_edit = '//*[@id="date-input-edit"]'
    _button_time = '//*[@id="time-input-create-how"]'
    _button_time_edit = '//*[@id="time-input-edit"]'
    _submit_button_task = '//*[@type="submit"]'
    _submit_button_edit_task = '//*[@class="EditTodo_button__ySCIK"][@type="submit"]'
    _edit_task = '//*[@id="edit-module"]//*[text() = "Изменить"]'
    _edited_task = '//*[@class="Success_ok__y8HHg"][text() = "ОК"]'
    _open_task = '//li[1]/ul/div/h4'
    _view_title_task = '//h1[@class="Review_title__AHmpO"]'
    _submit_task_created = '//*[@class="Success_ok__y8HHg"]'
    _list_tasks = '//*[@class="mt-2.5"]'
    _task_title = '//*[@class="mt-2.5"]//h4[@class="TodoItem_content__J_7bo"]'
    _first_task_title_edit = '//li[1]//button[1]/img'
    _opened_task = '//*[@class="EditTodo_wrapper___1B6a"]'
    _value_name = '//*[@id="edit-module"]//*[@placeholder="Заголовок"]'
    _value_description = '//*[@id="edit-module"]//*[@placeholder="Описание задачи"]'


    def __init__(self, driver):
        super().__init__(driver)
        self.generator = Generator()
        self.created_task_name = None
        self.edit_title_value = None

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

    @allure.step("Редактируем задачу")
    def edit_task_title(self):
        self.wait_page_loaded()
        self.wait_element_clickable(self._first_task_title_edit)
        self.driver.find_element(*self._first_task_title_edit).click()
        self.wait_element_clickable(self._opened_task)
        title_field = self.driver.find_element(*self._value_name)
        title_field.clear()
        edit_title_value = self.generator.generate_string()
        title_field.send_keys(edit_title_value)
        self.edit_title_value = edit_title_value
        self.driver.find_element(*self._submit_button_edit_task).click()
        self.wait_element_clickable(self._edit_task)
        self.driver.find_element(*self._edit_task).click()
        self.wait_element_clickable(self._edited_task)
        self.driver.find_element(*self._edited_task).click()

    # @allure.step("Редактируем описание")
    # def edit_description(self):
    #     self.wait_element_clickable(self._value_description)
    #     self.driver.find_element(*self._value_description).click()
    #     self.driver.find_element(*self._value_description).clear()
    #     self.driver.find_element(*self._value_description).click()
    #     edit_description_value = self.generator.generate_string()
    #     self.driver.find_element(*self._value_description).send_keys(edit_description_value)
    #     return edit_description_value
    #
    # @allure.step("Редактируем дату задачи")
    # def edit_date_task(self):
    #     current_date_edit = self.generator.get_current_date()
    #     date_field_edit = self.wait_element_clickable(self._button_date_edit)
    #     date_field_edit.send_keys(current_date_edit)
    #     return current_date_edit
    #
    # @allure.step("Редактируем время задачи")
    # def edit_time_task(self):
    #     current_time_edit = self.generator.get_current_time()
    #     time_field_edit = self.wait_element_clickable(self._button_time_edit)
    #     time_field_edit.send_keys(current_time_edit)
    #     time.sleep(5)
    #     self.driver.find_element(*self._submit_button_edit_task).click()
    #     self.wait_element_clickable(self._edit_task)
    #     self.driver.find_element(*self._edit_task).click()
    #     self.wait_element_clickable(self._edited_task)
    #     self.driver.find_element(*self._edited_task).click()
    #     return current_time_edit

    @allure.step("Проверяем отредактировануую задачу")
    def check_edit_task(self):
        self.wait_page_loaded()
        self.wait_element_clickable(self._open_task)
        self.driver.find_element(*self._open_task).click()
        view_title_task = self.driver.find_element(*self._view_title_task).text
        assert self.edit_title_value == view_title_task, \
            f"Ожидали '{self.edit_title_value}', получили '{view_title_task}'"