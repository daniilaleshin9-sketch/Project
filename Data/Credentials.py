import os
from dotenv import load_dotenv
load_dotenv()

class Credentials:
    LOGIN = os.getenv('LOGIN')
    PASSWORD = os.getenv('PASSWORD')