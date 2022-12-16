# import os for environment variable
import os
# import the time module to delay the code
import time
# import selenium which gets the automation done
from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.common import ElementClickInterceptedException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# get the location of the chrome driver path
from selenium.webdriver.support.wait import WebDriverWait

chrome_driver_path = '/Users/racool/Desktop/chromedriver'

user_name = os.getenv('USER')
password = os.getenv('PASSWORD')

link = 'https://www.instagram.com/'
influencer = 'python.learning'


class Instagram:
    def __init__(self):
        # create a webdriver object then assign the location for driver
        self.driver = webdriver.Chrome(chrome_driver_path)
        self.user = os.getenv('USER')
        self.password = os.getenv('PASSWORD')
        self.follower_list = []

    def logIn(self):
        self.driver.get(link)
        time.sleep(1)
        self.driver.find_element(By.NAME, 'username').send_keys(self.user)
        self.driver.find_element(By.NAME, 'password').send_keys(self.password)
        time.sleep(1)
        self.driver.find_element(By.CLASS_NAME, 'y3zKF').click()
        time.sleep(3)
        self.driver.find_element(By.CLASS_NAME, 'cmbtv').click()

    def find_followers(self):
        time.sleep(1)
        self.driver.find_elements(By.CSS_SELECTOR, '._a9-v ._a9-z button')[1].click()
        # self.driver.find_element(By.CLASS_NAME, '_aauy').send_keys(influencer)
        # time.sleep(2)
        self.driver.get(f'https://www.instagram.com/{influencer}')
        time.sleep(1)
        WebDriverWait(
            self.driver, 2).until(EC.element_to_be_clickable(
            (By.PARTIAL_LINK_TEXT, "followers"))).click()

        # self.driver.find_elements(By.CLASS_NAME, '_aa_5')[1].click() time.sleep(3) model =
        # self.driver.find_element(By.XPATH, '//*[@id="mount_0_0_ew"]/div/div/div/div[2]/div/div/div[1]/div/div['
        # '2]/div/div/div/div/div[2]/div/div/div[2]')
        pop_up_window = WebDriverWait(
            self.driver, 2).until(EC.element_to_be_clickable( (By.XPATH, "//*[@id='mount_0_0_ew']/div/div/div/div["
                                                                         "2]/div/div/div[1]/div/div["
                                                                         "2]/div/div/div/div/div[2]/div/div/div[2]")))

        # Scroll till Followers list is there
        while True:
            self.driver.execute_script(
                'arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;',
                pop_up_window)
            time.sleep(1)
        # for i in range(10):
        #     self.driver.execute_script(f"arguments[0].scrollTop = arguments[0].scrollHeight", model)

    def follower_lists(self):
        self.follower_list = self.driver.find_elements(By.CSS_SELECTOR, '._aano div div div button')
        return self.follower_list

    def follow(self):

        counter = 0
        for follow in range(100):
            self.follower_lists()
            time.sleep(2)
            if counter == 6:
                self.driver.execute_script(f"arguments[0].scrollTop = arguments[0].scrollHeight",
                                           self.follower_list[follow])
                time.sleep(3)
                counter = 0
            try:
                self.follower_list[follow].click()
            except ElementClickInterceptedException:
                self.driver.find_element(By.CLASS_NAME, '_a9_1').click()
            else:
                continue
            counter += 1


user1 = Instagram()
user1.logIn()
user1.find_followers()
