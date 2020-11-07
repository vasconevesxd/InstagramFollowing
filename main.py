from selenium import webdriver
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
        following = self._get_names()
        not_following_back = [user for user in following if user]
        print(not_following_back)

    def _get_names(self):

        sleep(2)

        user_path = self.driver.find_elements_by_class_name('FPmhX')
        
        numb_users_class = len(user_path)


        for x in range(numb_users_class):
            
            x += 1

            users_list = x


            self.driver.find_element_by_xpath('//a[@class="FPmhX notranslate  _0imsa "]' + '[' + str(x) + ']')\
                .click()
            
            sleep(2)
            
            self.driver.find_element_by_xpath("//a[contains(@href,'/following')]")\
                .click()
            
            sleep(2)
           
        
            last_ht, ht = 0, 1
            
            numb_following, y = 0, 0
            
            while last_ht != ht:
                last_ht = ht

                sleep(1)

                numb_following += len(user_path)
                
                sleep(2)
                
                #print("=>Index: " + str(y) + "Valor Total" + str(numb_following))

                while y != numb_following:               
                    
                    y += 1 

                    k = y + 1
                    print("=>" + str(k))
                            
                    scroll_box = self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/ul/div/li" + '[' + str(k) + ']')

                    ht = self.driver.execute_script('arguments[0].scrollIntoView(true);', scroll_box)

                    sleep(3)
                
                    #self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]/ul/div/li" + '[' + str(y) + ']' + "/div/div[3]/button")\
                    #    .click()
        
            sleep(2)    
            
            self.driver.get("https://instagram.com/username")
                
            sleep(2)
                
            self.driver.find_element_by_xpath("//a[contains(@href,'/following')]")\
                .click()

                            




               

           



        '''
        scroll_box = self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[2]")
        last_ht, ht = 0, 1
        while last_ht != ht:
            last_ht = ht
            sleep(1)
            ht = self.driver.execute_script("""
                arguments[0].scrollTo(0, arguments[0].scrollHeight); 
                return arguments[0].scrollHeight;
                """, scroll_box)
        links = scroll_box.find_elements_by_tag_name('a')
        names = [name.text for name in links if name.text != '']
        # close button

        self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div[1]/div/div[2]/button")\
            .click()

        return names
        '''





my_bot = InstaBot('username', '1231234')
my_bot.get_unfollowers('username')