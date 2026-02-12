import pytest
from pages import base_page
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Pages.login_page import LoginPage
from Pages.main_page import MainPage
from Data.Credentials import Credentials
from base.base_page import BasePage
import time


@pytest.fixture(autouse=True)
def driver(request):
    chrome_options = Options()
    chrome_options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(options=chrome_options)
    request.cls.driver = driver
    request.cls.login_page = LoginPage(driver)
    request.cls.main_page = MainPage(driver)
    yield driver
    driver.quit()

@pytest.fixture()
def auth_driver(driver):
    login_page = LoginPage(driver)
    login_page.open()
    login_page.login(Credentials.LOGIN)
    login_page.password(Credentials.PASSWORD)
    time.sleep(0.5)
    login_page.button_login()