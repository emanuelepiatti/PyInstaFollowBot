from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium import webdriver
from random import randrange
from minutemail import Mail
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
        users_creator(firefox_browser, 1)
        #login(firefox_browser)
        firefox_browser.quit()
    
    except Exception as e:
        print("ERROR")
        print(e)
        firefox_browser.quit()
    
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
    email = email_creator(browser)
    password = password_generator(15)
    
    print("-----TRYING------")
    print("username: " + username)
    print("name: " + name)
    print("surname: " + surname)
    print("email: " + email)
    print("password: " + password)

    browser.get("https://www.instagram.com/accounts/emailsignup")
    browser.set_window_size(867, 692)
    time.sleep(random.uniform(2, 3))

    number = 0
    account_created = False
    first_time = True
    while(account_created == False):
        browser.find_element(By.XPATH, '//button[text()="Only allow essential cookies"]').click()
        time.sleep(random.uniform(4, 5))
    
        emailOrPhone_field = browser.find_element(By.NAME, "emailOrPhone")
        fullName_field = browser.find_element(By.NAME, "fullName")
        username_field = browser.find_element(By.NAME, "username")
        password_field = browser.find_element(By.NAME, "password")
        submit_button = browser.find_element(By.CSS_SELECTOR, ".bkEs3:nth-child(1) > .sqdOP")

        emailOrPhone_field.click()
        emailOrPhone_field.send_keys(email)
        fullName_field.click()
        fullName_field.send_keys(name + " " + surname)
        username_field.click()
        username_field.send_keys(username)
        password_field.click()
        password_field.send_keys(password)
        submit_button.click()

        time.sleep(random.uniform(2, 4))

        birthday_date_filler(browser)
        #email_confirmation(browser, email)

        try:
            '''
            browser.find_element(By.CSS_SELECTOR, ".eiUFA")
            browser.find_element(By.ID, "igCoreRadioButtonageRadioabove_18").click()
            next_buttons = browser.find_elements_by_xpath("//*[contains(text(), 'Next')]")
            next_buttons[1].click()
            '''
            check_button = browser.find_elements(By.CLASS_NAME, "glyphsSpriteEmail_confirm u-__7")
            account_created = True
            first_time = False
            print("NEED EMAIL CONFIRMATION")
            
        except:
            print("NOPE")
            email = username + str(number) + "@gmail.com"
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
            print("email: " + email)
            print("password: " + password)

    time.sleep(random.uniform(10, 15))
    return {'username':username, 'password': password}

def birthday_date_filler(browser):
    print("birthday_date_filler")
    selects = browser.find_elements(By.CLASS_NAME, "h144Z  ")

    for i in range(len(selects)):
        select = selects[i]
        select = Select(select)

        if i == len(selects)-1:
            select.select_by_value('2000')
        else:
            select.select_by_value('1')

    time.sleep(random.uniform(2, 3))
    browser.find_element(By.XPATH, "//*[contains(text(), 'Next')]").click()

    print("birthday_date_filler OK")

def email_creator(browser):
    print("email_creator")
    browser.get("https://10minutemail.net")
    time.sleep(random.uniform(2, 3))
    new_email = browser.find_element(By.ID, "fe_text").get_attribute('value')

    return new_email

def email_confirmation(browser, email):
    print("op")

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
