from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os

INSTAGRAM_NAME = os.environ["INSTAGRAM_NAME"]
INSTAGRAM_PASSWORD = os.environ["PASSWORD"]
SIMILAR_ACCOUNT = "healthy.cookingrecipes"


CHROME_DRIVER_PATH = "C://Development/chromedriver.exe"

class InstaFollower:
    def __init__(self, path):
        self.driver = webdriver.Chrome(path)
        self.element_inside_popup = None

    def login(self):
        self.driver.get("https://www.instagram.com/")

        accept_all_cookies = self.driver.find_element_by_xpath('/html/body/div[4]/div/div/button[1]')
        accept_all_cookies.click()

        time.sleep(2)
        name = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[1]/div/label/input')
        name.send_keys(INSTAGRAM_NAME)

        password = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[2]/div/label/input')
        password.send_keys(INSTAGRAM_PASSWORD)

        log_in = self.driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]')
        log_in.click()

        time.sleep(3)

        dont_save_login_info_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/div/div/div/button')
        dont_save_login_info_button.click()
        # If doesnt work- add time

        time.sleep(2)
        print("I pressed on do_not_turn_on_notifications")
        do_not_turn_on_notifications = self.driver.find_element_by_css_selector("button.aOOlW.HoLwm")
        do_not_turn_on_notifications.click()
        self.driver.maximize_window()

    def find_followers(self):
        time.sleep(2)
        print("Search initiated (in find_followers function)")
        search_button = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
        search_button.send_keys(SIMILAR_ACCOUNT)
        search_button.send_keys(Keys.RETURN)

        time.sleep(3)

        print("Pressed on account")
        account = self.driver.find_element_by_class_name('-qQT3')
        account.click()

        time.sleep(3)

        print("Pressed followers link")
        link_to_followers = self.driver.find_element_by_xpath('//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        link_to_followers.click()

        time.sleep(3)

        print("Identifying element_inside_popup")
        self.element_inside_popup = self.driver.find_element_by_xpath('/html/body/div[6]/div/div/div[2]')
        print("Scrolling down")
        count = 0
        for i in range(100):
            try:
                self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", self.element_inside_popup)
                time.sleep(2)
                count += 1
                print(count)

            except:
                print("Scrolling should be finished now. Please check and insert Except code")

    def follow(self):
        buttons = self.driver.find_elements_by_css_selector('li button')
        print("Number of buttons collected is: ")
        print(len(buttons))
        followers_added = 0
        for button in buttons:
            try:
                time.sleep(1)
                button.click()
                followers_added += 1
                print("Followers added: ", followers_added)
            except:
                cancel_button = self.driver.find_element_by_xpath('/html/body/div[7]/div/div/div/div[3]/button[2]')
                cancel_button.click()
                

bot = InstaFollower(CHROME_DRIVER_PATH)
bot.login()
bot.find_followers()
bot.follow()