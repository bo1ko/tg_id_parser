from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from modules import Authorization
from modules import UsersHandler

from fake_useragent import UserAgent

import time


def main():
    options = Options()
    options.add_argument(f'user-agent={UserAgent().random}')
    options.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument("--log-level=3")
    options.add_argument("--headless")  # Запуск без графічного інтерфейсу
    options.add_argument("--disable-gpu")
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.get('https://web.telegram.org/a/')

    wait = WebDriverWait(driver, 10)

    number = str(input('Введіть номер телефону: '))

    Authorization(driver, wait).login_by_number(number, 'Ukraine')
    time.sleep(3)

    wait = WebDriverWait(driver, 3)
    user_handler = UsersHandler(driver, wait)
    user_handler.find_users_id()


if __name__ == '__main__':
    main()
