from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
import sys
import time
import site

#HELPFUL LINKS
# https://selenium-python.readthedocs.io/locating-elements.html

def run():
    firefox_browser = browser()
    accountCreate(firefox_browser)
    firefox_browser.quit()
    
def login(browser, username, password):
    print("login")
    browser.get("https://www.instagram.com/accounts/login")
    time.sleep(3)
    username_field = browser.find_element(By.NAME, "username")
    password_field = browser.find_element(By.NAME, "password")
    username_field.clear()
    password_field.clear()
    username_field.send_keys(username)
    password_field.send_keys(password)
    password_field.send_keys(Keys.ENTER)

    print(check_login(browser))

def check_login(browser):
    print("check_login")
    time.sleep(5)
    logged = False
    test = check_element_exist("ID", "slfErrorAlert")
    print("POOOOOOOOOOOOO" + str(test))

    try:
        print("try")
        login = browser.find_element(By.ID, "slfErrorAlert")

    except:
        print("except")
        try:
            print("try1")
            verification_code_required = browser.find_element(By.ID, "verificationCodeDescription")
            two_factor_authentication(browser)
            try:
                print("try2")
                try:
                    myElem = WebDriverWait(browser, 120).until(
                        EC.presence_of_element_located((By.CLASS_NAME, "_6q-tv")))
                    print("Page is ready!")

                except TimeoutException:
                    print("Loading took too much time!")

                sooo = browser.find_element(By.CLASS_NAME, "_6q-tv")
                logged = True
            except Exception as e:
                print("except2")
                print(e)

        except:
            print("except1")
            
            
    return logged

def check_element_exist(search_by, elemnt):
    #TODO CHECK IF WORKS (NOT SURE)
    exist = False
    search_by = "By." + str(search_by)
    print("search_by ->" + str(search_by))

    try:
        element = browser.find_element(search_by, elemnt)
        exist = True
    except:
        pass

    return exist
    
    
def two_factor_authentication(browser):
    print("two_factor_authentication")
    authentication_code = input("Authentication code: ")
    code_field = browser.find_element(By.NAME, "verificationCode")
    code_field.send_keys(authentication_code)
    code_field.send_keys(Keys.ENTER)

def os_detect():
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
        path = "./geckodriver/" + os_detected
        browser = webdriver.Firefox(options=options, executable_path= path)
        return browser

    else:
        print("ERROR: type of operating system not detected")

def accountCreate(browser):
    browser.get("https://www.instagram.com/accounts/emailsignup/")
    browser.set_window_size(550, 691)
    time.sleep(5)
    browser.find_element(By.NAME, "emailOrPhone").click()
    browser.find_element(By.NAME, "emailOrPhone").send_keys(email(browser))
    browser.find_element(By.NAME, "fullName").click()
    browser.find_element(By.NAME, "fullName").send_keys("sdvsdvsdvsd")
    browser.find_element(By.NAME, "username").click()
    browser.find_element(By.NAME, "username").send_keys("sdvsdvsdvs")
    browser.find_element(By.NAME, "password").click()
    browser.find_element(By.NAME, "password").send_keys("sdvsdvdsv")
    browser.find_element(By.CSS_SELECTOR, ".bkEs3:nth-child(1) > .sqdOP").click()


def email(browser):
    browser.get("https://10minutemail.net/?lang=en")
    browser.set_window_size(867, 692)
    time.sleep(5)
    email = browser.find_element(By.ID, "fe_text").get_attribute("value")
    return email

    
if __name__ == "__main__":
    run()
