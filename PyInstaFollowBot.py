from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from random import randrange
import datetime
import secrets
import random
import string
import time
import site
import sys


def run():

    try:
        firefox_browser = browser()
        users_creator(firefox_browser, 2)
        #login(firefox_browser)
        firefox_browser.quit()
    
    except Exception as e:
        print("ERROR")
        print(e)
        #firefox_browser.quit()
    
def os_detect():
    #TODO add all mac processors M and Intel
    print("os_detect")
    os = None
    if sys.platform.startswith('linux'):
        os = "linux"

    elif sys.platform.startswith('win32'):
        os = "win32"

    elif sys.platform.startswith('darwin'):
        os = "darwin"

    return os

def browser():
    print("browser")
    os_detected = os_detect()
    if os_detected:
        options = Options()
        #options.headless = True
        options.headless = False
        profile = webdriver.FirefoxProfile()
        profile.set_preference('intl.accept_languages', 'en-US, en')
        path = "./geckodriver/" + os_detected
        browser = webdriver.Firefox(firefox_profile=profile, options=options, executable_path= path)
        return browser

    else:
        print("ERROR: operating system not detected")

def login(browser):
    created_users = open('./created_users.txt.dat', 'w+')
    lines = created_users.readlines()
    for line in lines:
        splitted = line.split("-")
        username = splitted[0]
        password = splitted[1]
        time.sleep(random.uniform(4, 5))
        
        username_field = browser.find_element(By.NAME, "username")
        password_field = browser.find_element(By.NAME, "password")
        username_field.clear()
        password_field.clear()
        username_field.click()
        username_field.send_keys(username)
        password_field.click()
        password_field.send_keys(password)
        browser.find_element(By.CSS_SELECTOR, ".sqdOP > .Igw0E").click()
        time.sleep(random.uniform(3, 4))
        #TODO whatever you want

def insta_user_create(browser):
    names_files = open("./data/names.txt")
    lines = names_files.readlines()

    lines_count = 0
    for line in lines:
        lines_count += 1

    name = lines[randrange(lines_count)]
    name = name.rstrip("\n")
    
    surnames_files = open("./data/surnames.txt")
    lines = surnames_files.readlines()

    lines_count = 0
    for line in lines:
        lines_count += 1

    surname = lines[randrange(lines_count)]
    surname = surname.rstrip("\n")

    username = str(name + surname)
    username = username.lower() + "lalala"
    e_mail = username + "@gmail.com"
    password = password_generator(15)

    print("-----TRYING------")
    print("username: " + username)
    print("name: " + name)
    print("surname: " + surname)
    print("email: " + e_mail)
    print("password: " + password)

    browser.get("https://www.instagram.com/accounts/emailsignup")
    browser.set_window_size(867, 692)
    time.sleep(random.uniform(2, 3))

    number = 0
    account_created = False
    while(account_created == False):
        browser.find_element(By.XPATH, '//button[text()="Only allow essential cookies"]').click()
        time.sleep(random.uniform(4, 5))
    
        emailOrPhone_field = browser.find_element(By.NAME, "emailOrPhone")
        fullName_field = browser.find_element(By.NAME, "fullName")
        username_field = browser.find_element(By.NAME, "username")
        password_field = browser.find_element(By.NAME, "password")
        submit_button = browser.find_element(By.CSS_SELECTOR, ".bkEs3:nth-child(1) > .sqdOP")

        emailOrPhone_field.click()
        emailOrPhone_field.send_keys(e_mail)
        fullName_field.click()
        fullName_field.send_keys(name + " " + surname)
        username_field.click()
        username_field.send_keys(username)
        password_field.click()
        password_field.send_keys(password)
        submit_button.click()

        time.sleep(random.uniform(2, 4))

        birthday_date_filler(browser)

        try:
            browser.find_element(By.CSS_SELECTOR, ".eiUFA")
            browser.find_element(By.ID, "igCoreRadioButtonageRadioabove_18").click()
            next_buttons = browser.find_elements_by_xpath("//*[contains(text(), 'Next')]")
            next_buttons[1].click()
            account_created = True
            print("CREATED")
            
        except:
            print("NOPE")
            e_mail = username + str(number) + "@gmail.com"
            username = username + str(number)
            number += 1

            emailOrPhone_field.clear()
            fullName_field.clear()
            username_field.clear()
            password_field.clear()

            print("-----TRYING------")
            print("username: " + username)
            print("name: " + name)
            print("surname: " + surname)
            print("email: " + e_mail)
            print("password: " + password)

    time.sleep(random.uniform(10, 15))
    return {'username':username, 'password': password}

def birthday_date_filler(browser):
    selects = browser.find_element(By.XPATH, "//select[@class='h144Z  ']")
    
    print(select)
    #select.select_by_value('1')

def password_generator(lenght):
    alphabet = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(alphabet) for i in range(lenght))
    return password

def users_creator(browser, quantity):
    for x in range(0, quantity):
        credentials = insta_user_create(browser)
        f = open('created_users.txt', "a")
        f.write(credentials['username'] + "-" + credentials['password'] + "\n")
        f.close()

if __name__ == "__main__":
    run()
