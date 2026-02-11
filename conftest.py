import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from Pages.login_page import LoginPage
from Pages.main_page import MainPage


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

