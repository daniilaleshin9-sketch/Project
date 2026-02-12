import random
import string
from faker import Faker
from datetime import datetime

fake = Faker()

class Generator:
    def generate_string(self, length=10):
        """Генерирует случайную строку заданной длинны"""
        letters = string.ascii_letters
        result_str = ''
        for _ in range(length):
            result_str += random.choice(letters)
        return result_str

    def generate_number(self, min_val=10, max_val=100):
        """Генерирует случайное число в заданном диапозоне"""
        return random.randint(min_val, max_val)

    def generate_email(self, domain='example.com'):
        """Генерирует случайный майл"""
        email = fake.email()
        return f'{email}@{domain}'

    def generate_phone(self, country_code='+1'):
        """Генерирует случайный номер телефона с указанным кодом"""
        return f"{country_code} {fake.msisdn()[-10:]}"

    def get_current_date(self):
        """Возвращает текущую дату в формате ДД.ММ.ГГГГ"""
        return datetime.now().strftime("%d.%m.%Y")

    def get_current_time(self):
        """Возвращает текущее время в формате ЧЧ.ММ"""
        return datetime.now().strftime("%H.%M")
