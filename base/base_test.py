from Pages.login_page import LoginPage
from Pages.main_page import MainPage
from Data.Credentials import Credentials
from utiles.generators import Generator

class BaseTest:

        generator = Generator()
        login_page = None
        main_page = None
        credentials_page = None
        driver = None


