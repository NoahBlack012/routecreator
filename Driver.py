from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class driver:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.PATH = "C:\Program Files (x86)\chromedriver.exe"
        self.driver = webdriver.Chrome(self.PATH)

    def run_driver(self):
        try:
            self.driver.get("https://www.google.ca/maps")
            time.sleep(3)
            direction_button = self.driver.find_element_by_xpath('//*[@id="searchbox-directions"]')
            direction_button.click()
            time.sleep(8)
            start_box = self.driver.find_element_by_xpath('/html/body/jsl/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[1]/div[2]/div/div/input')
            for i in range(13):
                start_box.send_keys(Keys.BACK_SPACE)
            start_box.send_keys(self.start)
            destination_box = self.driver.find_element_by_xpath('/html/body/jsl/div[3]/div[9]/div[3]/div[1]/div[2]/div/div[3]/div[1]/div[2]/div[2]/div/div/input')
            destination_box.send_keys(self.end)
            destination_box.send_keys(Keys.ENTER)
            time.sleep(3)
            url = self.driver.current_url
            drive_btn = self.driver.find_element_by_xpath('//*[@id="omnibox-directions"]/div/div[2]/div/div/div[1]/div[2]/button')
            drive_btn.click()
            time.sleep(5)
            trip_time = self.driver.find_element_by_xpath('//*[@id="section-directions-trip-0"]/div[1]/div[1]/div[1]/div[1]/span[1]').text
            distance = self.driver.find_element_by_xpath('//*[@id="section-directions-trip-0"]/div[1]/div[1]/div[1]/div[2]/div').text
            details_btn = self.driver.find_element_by_xpath('//*[@id="section-directions-trip-0"]/div[1]/div[1]/div[4]/button')
            details_btn.click()
            time.sleep(2)
            directions = self.driver.find_element_by_xpath('//*[@id="pane"]/div/div[1]/div/div/div[5]/div').text
            directions = directions[:-277]
            self.driver.quit()
        except:
            self.driver.quit()
            trip_time = ''
            distance = ''
            directions = '' 
            url = ''
        return trip_time, distance, directions, url
