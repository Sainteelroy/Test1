from selenium import webdriver
from time import sleep

class webauto():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def open(self):
        self.driver.get('https://www.speedtest.net/')
        sleep(5)
        go = self.driver.find_element_by_xpath('//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a')
        go.click()

        sleep(50)
        self.driver.quit()


bot = webauto()
bot.open()
