import os
from dotenv import load_dotenv

load_dotenv()

STAGE = os.getenv('STAGE')

class Urls:

    HOST = f"http://{STAGE}:6700"
    LOGIN_PAGE = f"{HOST}/auth/login"

print(Urls.LOGIN_PAGE)
