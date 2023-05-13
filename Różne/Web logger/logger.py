import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import logger

class Browser:
    browser, service = None, None 

    def __init__(self, driver: str):
        self.service = Service(driver)
        self.browser = webdriver.Chrome(service=self.service)
    
    def open_page(self, url: str):
        self.browser.get(url)
    
    def close_browser(self):
        self.browser.close()
        
    def add_input(self, by: By , value: str, text: str):
        field = self.browser.find_element(by=by, value=value)
        field.send_keys(text)
        time.sleep(1)

    def click_button(self, by: By , value: str):
        button= self.browser.find_element(by=by, value=value)
        button.click()
        time.sleep(1)

    def login_linkedin(self, username: str, password: str):
        self.add_input(by=By.ID, value='session_key', text=username)
        self.add_input(by=By.ID, value='session_password', text=password)
        self.click_button(by=By.CLASS_NAME, value='sign-in-form__submit-button')

if __name__ == '__main__':
    browser = Browser('Drivers\chromedriver.exe')

    browser.open_page('https://pl.linkedin.com/')
    time.sleep(3)
    
    browser.login_linkedin(username='janglin123456@gmail.com', password='janglin2137')
    time.sleep(5)
    
    browser.close_browser()     