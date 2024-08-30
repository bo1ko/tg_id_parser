from selenium.webdriver.common.by import By

from modules.actions import Actions

import time

class Search(Actions):
    def __init__(self, driver, wait):
        super().__init__(driver, wait)

    def _has_focus(self):
        if self._find_element('//*[@id="LeftMainHeader"]/div[2]').get_attribute('class') != 'SearchInput has-focus':
            self._click_element_by_id('telegram-search-input')

    def _user_search(self, username):
        self._has_focus()
        self._find_element_by_id('telegram-search-input').clear()
        self._type_text_by_id(username, 'telegram-search-input')
        
        while True:
            time.sleep(0.3)

            if self._find_element_by_class('section-heading'):
                try:
                    self._driver.find_element(By.XPATH, '//*[@id="LeftColumn-main"]/div[2]/div[2]/div/div[2]/div/div/h3/a').click()
                except:
                    pass

                for element in self._find_elements_by_class('search-result'):
                    if username in element.text:
                        return element.find_element(By.CLASS_NAME, 'Avatar').get_attribute("data-peer-id")
            elif self._find_element_by_class('NothingFound'):
                return 'user not found'
            else:
                return 'Error'
                    
