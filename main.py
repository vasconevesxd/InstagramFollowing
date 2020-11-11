from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from time import sleep



class InstaBot:
    def __init__(self, username, pw):
        self.driver = webdriver.Chrome(executable_path='C:\chromedriver\chromedriver.exe')
        self.username = username
        self.pw = pw
        self.driver.get("https://instagram.com")
        sleep(2)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Accept')]")\
            .click()
        sleep(2)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]")\
            .send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]")\
            .send_keys(pw)
        self.driver.find_element_by_xpath('//button[@type="submit"]')\
            .click()
        sleep(4)
       

    def get_unfollowers(self,username):

        self.driver.get("https://instagram.com/" + username)
        sleep(2)
        self.driver.find_element_by_xpath("//a[contains(@href,'/following')]")\
            .click()
        self._get_names()
       


    def _get_names(self):

        sleep(2)

        user_path = self.driver.find_elements_by_css_selector('.PZuss > li')
        print(user_path)
        numb_users_class = len(user_path)
        

        for x in range(numb_users_class):
            
            x += 1

            if numb_users_class-1 == x:
                
                user_path = self.driver.find_elements_by_css_selector('.PZuss > li')
                numb_users_class = len(user_path)

            elem = self.driver.find_element_by_css_selector('.PZuss > li:nth-child(' + str(x) + ') a')

            if elem.is_displayed():
 
                self.driver.execute_script('arguments[0].scrollIntoView(true);', elem)
                sleep(4)
                print("=>Index: " + str(x) + "Valor Total" + str(numb_users_class))
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
            
            user_path = self.driver.find_elements_by_css_selector('.PZuss > li')
            numb_following = len(user_path)
            print(numb_following)
                
            sleep(2)
                

            for y in range(numb_following):          
                
                y += 1  

                if numb_following-1 == y:
                    user_path = self.driver.find_elements_by_css_selector('.PZuss > li')
                    numb_following = len(user_path)
               

                try:

                    element = self.driver.find_element_by_css_selector('.PZuss > li:nth-child(' + str(y) + ') .sqdOP.L3NKy.y3zKF')

                    if element.is_displayed():
 
                        self.driver.execute_script('arguments[0].scrollIntoView(true);', element)
                        sleep(4)
                        print("=>Index: " + str(y) + "Valor Total" + str(numb_following))
                        self.driver.find_element_by_css_selector('.PZuss > li:nth-child(' + str(y) + ' ) button')\
                        .click()
                        print("Element found")
                   
                    else:
                        print("Element not found")
                    
                        sleep(3)

                except NoSuchElementException:
                    print("No element found")
                
              
            sleep(2)    
            
            self.driver.get("https://instagram.com/username")
                
            sleep(3)

            self.driver.find_element_by_xpath("//a[contains(@href,'/following')]")\
                .click()
            sleep(3)
                            


my_bot = InstaBot('username', '1231234')
my_bot.get_unfollowers('username')