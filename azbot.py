#chromer driver for chrome events and Selnium for automate calls
from selenium import webdriver
#time package to use sleep for pausing while the page event loads
from time import sleep

#Create a file secret.py
#uid = '[emailid]'
#pwd= '[password]'
from secrets import uid, pwd

class azbot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def open(self):
        self.driver.get('https://account.amazon.jobs/en-US/login?relay=%2Fen-US')
        sleep(1)

        email_in = self.driver.find_element_by_xpath('/html/body/main/div[2]/div/div/div/div/div/div[1]/div/div/input')
        email_in.send_keys(uid)

        continue_btn = self.driver.find_element_by_xpath('/html/body/main/div[2]/div/div/div/div/div/button[1]')
        continue_btn.click()
        sleep(10)

        password_in = self.driver.find_element_by_xpath('/html/body/div/div/div[2]/div[2]/div[1]/div/div[1]/form/div[3]/div[1]/input')
        password_in.send_keys(pwd)

        continue_btn = self.driver.find_element_by_xpath('/html/body/div/div/div[2]/div[2]/div[1]/div/div[1]/form/div[6]/button')
        continue_btn.click()

        sleep(100)
        self.driver.quit()


bot = azbot()
bot.open()
