import time
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By

email='janglin123456@gmail.com'
password='Janglin2137'

class Browser:
    browser, service = None, None 

    def __init__(self, driver: str):
        self.service = Service(driver)
        self.browser = webdriver.Edge(service=self.service)
    
    def open_page(self, url: str):
        self.browser.get(url)
    
    def close_browser(self):
        self.browser.close()
        
    def add_input(self, by: By , value: str, text: str):
        field = self.browser.find_element(by=by, value=value)
        field.clear()
        field.send_keys(text)
        time.sleep(0.5)

    def click_button(self, by: By , value: str):
        button= self.browser.find_element(by=by, value=value)
        button.click()
        time.sleep(1)

    def login_XS(self, username: str, password: str):
        self.add_input(by=By.NAME, value="xslogin", text=username)
        self.add_input(by=By.NAME, value="xspass", text=password)
        self.click_button(by=By.CSS_SELECTOR, value="#containment-wrapper > div.xs-switch-container.ng-scope > div.xs-login-with-timeline-wrapper.ng-isolate-scope > div > div.xs-login-error-responsive.xs-login-with-timeline-error-responsive > div.xs-login-container > div > div > form > div:nth-child(4) > input")
    def buy(self, quan: float):

        self.add_input(by=By.CSS_SELECTOR, value="#chartPanelsContainer > xchart-panel > div > div.chart-ct-toolbar.ng-scope > span.chart-ct-container.ng-scope > click-and-trade-mini-panel > div > div > div > form > span > input", text=str(quan))
        self.click_button(by=By.CSS_SELECTOR,value="#chartPanelsContainer > xchart-panel > div > div.chart-ct-toolbar.ng-scope > span.chart-ct-container.ng-scope > click-and-trade-mini-panel > div > button.xui-btn.xui-btn-ct-buy")
browser = Browser('Drivers\msedgedriver.exe')

browser.open_page('https://xstation5.xtb.com/?branch=pl#/_/login')
time.sleep(3)
    
browser.login_XS(username=email, password=password)
time.sleep(5)
browser.buy(1)
time.sleep(5)
