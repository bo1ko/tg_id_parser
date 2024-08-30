import pickle
import os


class SaveAuthorization:
    
    def __init__(self, driver):
        self._driver = driver
        
    def _load_local_storage(self, number):
        if os.path.exists(f'sessions/{number}.pkl'):
            with open(f'sessions/{number}.pkl', "rb") as file:
                return pickle.load(file)

        return None

    def _save_local_storage(self, number):
        local_storage_data = self._driver.execute_script("""
            let items = {};
            for (let i = 0; i < window.localStorage.length; i++) {
                var key = window.localStorage.key(i);
                items[key] = window.localStorage.getItem(key);
            }
            return items;
        """)

        with open(f'sessions/{number}.pkl', "wb") as file:
            pickle.dump(local_storage_data, file)
