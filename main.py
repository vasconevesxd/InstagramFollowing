from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep
from dotenv import load_dotenv #load_dotenv will be used to load the .env file to the environment variables.
import os #os will be used to refer to those variables in the code. Let’s start with

load_dotenv('.env') #load_dotenv. This will load the .env file.

USERNAME = os.environ.get("USER")
SECRET_KEY = os.environ.get("PASSWORD")
CHROME_URL = os.environ.get("CHROME_URL")

class InstaBot:
    def __init__(self, username, pw):

        self.driver = webdriver.Chrome(executable_path=CHROME_URL)

        self.username = username
        self.pw = pw

        self.driver.get("https://instagram.com")
        sleep(2)

        self.driver.find_element_by_xpath("//button[contains(text(), 'Accept')]")\
            .click()
        sleep(2)

        #Login with your credentials
        self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
            .send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
            .send_keys(pw)
        self.driver.find_element_by_xpath('//button[@type="submit"]')\
            .click()

        sleep(4)

    def get_following(self, username):

        #Open your following list on your instagram profile
        self.driver.get("https://instagram.com/" + username)
        sleep(2)
        self.driver.find_element_by_xpath("//a[contains(@href,'/following')]")\
            .click()
        self._get_follow(username)

    def _get_follow(self, username):

        sleep(2)

        user_path = self.driver.find_elements_by_css_selector('.PZuss > li')
        numb_users_class = len(user_path)

        for x in range(numb_users_class):

            x += 1

            if numb_users_class-1 == x:

                user_path = self.driver.find_elements_by_css_selector(
                    '.PZuss > li')
                numb_users_class = len(user_path)

            elem = self.driver.find_element_by_css_selector(
                '.PZuss > li:nth-child(' + str(x) + ') a')

            #if element exists scroll element by element and click on the user
            if elem.is_displayed():

                self.driver.execute_script(
                    'arguments[0].scrollIntoView(true);', elem)
                sleep(4)

                self.driver.find_element_by_css_selector('.PZuss > li:nth-child(' + str(x) + ') a')\
                    .click()
                print("Element found")

            else:
                print("Element not found")

            sleep(3)

           
            self.driver.find_element_by_xpath("//a[contains(@href,'/following')]")\
                .click()

            sleep(2)

            numb_following, y = 0, 0

            user_path = self.driver.find_elements_by_css_selector(
                '.PZuss > li')
            numb_following = len(user_path)

            sleep(2)

            for y in range(numb_following):

                y += 1

                if numb_following-1 == y:
                    user_path = self.driver.find_elements_by_css_selector(
                        '.PZuss > li')
                    numb_following = len(user_path)

                try:

                    element = self.driver.find_element_by_css_selector(
                        '.PZuss > li:nth-child(' + str(y) + ') .sqdOP.L3NKy.y3zKF')

                    if element.is_displayed():

                        self.driver.execute_script(
                            'arguments[0].scrollIntoView(true);', element)
                        sleep(4)

                        self.driver.find_element_by_css_selector('.PZuss > li:nth-child(' + str(y) + ' ) button')\
                            .click()
                        print("Element found")

                    else:
                        print("Element not found")

                        sleep(3)

                except NoSuchElementException:
                    print("No element found")

            sleep(2)

            self.driver.get("https://instagram.com/" + username)

            sleep(3)

            self.driver.find_element_by_xpath("//a[contains(@href,'/following')]")\
                .click()
            sleep(3)


my_bot = InstaBot(USERNAME, SECRET_KEY)
my_bot.get_following(USERNAME)
