from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

class InstagramBot:
    def __init__(self, username, password):
        '''This function passes the browser initialization parameters'''
        self.username = username
        self.password = password
        firefoxProfile = webdriver.FirefoxProfile()
        firefoxProfile.set_preference("intl.accept_languages", "pt,pt-BR")
        firefoxProfile.set_preference("dom.webnotifications.enabled", False)
        self.driver = webdriver.Firefox(
            firefox_profile=firefoxProfile, executable_path=r"geckodriver"
        )

    def login(self):
        '''function defined to log in to the Instagram home page'''
        driver = self.driver
        driver.get("https://www.instagram.com")
        time.sleep(3)

        user_element = driver.find_element_by_xpath(
            "//input[@name='username']")
        user_element.clear()
        user_element.send_keys(self.username)
        time.sleep(3)

        password_element = driver.find_element_by_xpath(
            "//input[@name='password']")
        password_element.clear()
        password_element.send_keys(self.password)
        time.sleep(3)

        password_element.send_keys(Keys.RETURN)
        time.sleep(5)
        self.comente_na_foto()

    @staticmethod
    def type_like_a_person(sentence, single_input_field):
        '''This code will basically allow you to simulate typing like a person'''
        print("Digitando comentário...")
        for letter in sentence:
            single_input_field.send_keys(letter)
            time.sleep(random.randint(1,3) / 30)
    
    def comente_na_foto(self):
        driver = self.driver
        '''add the publication link inside the parentheses in "driver.get"'''
        driver.get("https://www.instagram.com/p/")
        cont = 0
        while (cont < 2 ):
            '''the repeat loop is defined in the counter if you wanted to add a limited number of comments add a sum to each comment'''
            '''cont += 1'''
            try:
                '''add the desired comments to the list'''
                comments = ["comments"]
                driver.find_element_by_css_selector("[placeholder='Adicione um comentário...']").click()
                comment_input_box = driver.find_element_by_css_selector("[placeholder='Adicione um comentário...']")
                time.sleep(random.randint(2, 5))
                self.type_like_a_person(
                random.choice(comments), comment_input_box)
                time.sleep(random.randint(2, 5))
                comment_input_box.send_keys(Keys.RETURN)
                time.sleep(random.randint(2, 5))
                
            except Exception as e:
                print(e)
                time.sleep(random.randint(2, 5))
                
        else :
            print('ok')

'''Enter your Instagram username and password below'''
user = InstagramBot("user", "password")
user.login()