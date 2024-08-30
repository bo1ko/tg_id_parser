from modules.actions import Actions
from modules.save_authorization import SaveAuthorization

import time
import random


class Authorization(Actions):

    def __init__(self, driver, wait):
        super().__init__(driver, wait)

    def login_by_number(self, number, country):

        if len(number) > 9:
            number = number[-9:]
        elif len(number) != 9:
            print('Номер містить менше 9 цифр!\n')
        
        if not number.isdigit():
            print('Номер має містити тільки цифри\n')
            return False

        local_storage_data = SaveAuthorization(self._driver)

        if local_storage_data._load_local_storage(number):
            for key, value in local_storage_data._load_local_storage(number).items():
                self._driver.execute_script(
                    f"window.localStorage.setItem('{key}', '{value}');")

            self._driver.refresh()
            print('Авторизація пройшла успішно!')
        else:
            input()
            self._sleep_time()
            self._click_element('//*[@id="auth-qr-form"]/div/button')

            self._sleep_time()
            self._click_element('//*[@id="sign-in-phone-code"]')

            self._sleep_time()
            self._type_text(country, '//*[@id="sign-in-phone-code"]')

            self._sleep_time()
            self._click_element(
                '//*[@id="auth-phone-number-form"]/div/form/div[1]/div[2]/div[2]/div')

            self._sleep_time()
            self._type_text(number, '//*[@id="sign-in-phone-number"]')

            self._sleep_time()
            self._click_element(
                 '//*[@id="auth-phone-number-form"]/div/form/button[1]')

            while True:
                code = input('Введіть код: ')

                if len(code) != 5:
                    print('Код має мати 5 цифр!')
                    continue
                elif not code.isdigit():
                    print('Код має містити тільки цифри!')
                    continue

                self._type_text(code, '//*[@id="sign-in-code"]')
                time.sleep(1)

                if self._find_element_by_id('Main'):
                    print('\nАвторизація пройшла успішно!')
                    local_storage_data._save_local_storage(number)
                    break
                elif self._find_element('//*[@id="auth-code-form"]/div/div[2]/label').text == 'Invalid code.':
                    print('Невірний код!')
                    self._find_element('//*[@id="sign-in-code"]').clear()

                    continue
                else:
                    print('ERROR')

    def _sleep_time(self):
        return time.sleep(random.uniform(0.5, 1))
