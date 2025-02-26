from selenium import webdriver
import config
class BrowDriver:
    driver = None
    @classmethod
    def get_driver(cls):
        if cls.driver is None:
            cls.driver = webdriver.Chrome()
            cls.driver.get(config.url)
            cls.driver.maximize_window()
            cls.driver.implicitly_wait(10)
        return cls.driver
    @classmethod
    def quit_driver(cls):
        if cls.driver is not None:
            cls.driver.quit()
            cls.driver = None


