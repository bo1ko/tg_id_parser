from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Actions:

    def __init__(self, driver, wait):
        self._driver = driver
        self._wait = wait
    
    def _click_element(self, xpath):
        self._wait.until(EC.presence_of_element_located((By.XPATH, xpath))).click()
    

    def _click_element_by_id(self, id):
        self._wait.until(EC.presence_of_element_located((By.ID, id))).click()

    def _find_element(self, xpath):
        try:
            return self._wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
        except:
            return False
    
    def _find_element_by_class(self, _class):
        try:
            return self._wait.until(EC.presence_of_element_located((By.CLASS_NAME, _class)))
        except:
            return False
    
    def _find_elements_by_class(self, _class):
        try:
            return self._wait.until(EC.presence_of_all_elements_located((By.CLASS_NAME, _class)))
        except:
            return False

    def _find_element_by_id(self, id):
        try:
            return self._wait.until(EC.presence_of_element_located((By.ID, id)))
        except:
            return False

    def _type_text(self, text, xpath):
        self._wait.until(EC.presence_of_element_located((By.XPATH, xpath))).send_keys(text)

    def _type_text_by_id(self, text, id):
        self._wait.until(EC.presence_of_element_located((By.ID, id))).send_keys(text)
