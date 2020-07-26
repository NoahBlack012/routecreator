from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class webdriver:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.driver = webdriver.Chrome()

    def run_webdriver(self):
        self.driver.get("http://www.python.org")

a = webdriver("a", "b")
a.run_webdriver()
