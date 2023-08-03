from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
def launch_browser(browser_name):
    browser_name = browser_name.lower()

    if browser_name == 'chrome':
        driver = webdriver.Chrome()
    elif browser_name == 'firefox':
        # driver = webdriver.Firefox()
        options = webdriver.FirefoxOptions()
        options.binary_location = r"C:\Users\vicky\PycharmProjects\orangelogin\geckodriver.exe"
        driver = webdriver.Firefox(options=options)
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")
    return driver
def login(driver,name,pas):
    driver.maximize_window()
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
       # Find the username input element and send keys
    element = WebDriverWait(driver, 30).until(
        EC.presence_of_element_located((By.XPATH, '//input[@placeholder="Username"]'))
    )
    username = driver.find_element(By.XPATH, '//input[@placeholder="Username"]')
    username.send_keys(name)
    # time.sleep(20)
    # Add any additional test steps here, like finding the password field and entering the password
    password = driver.find_element(By.XPATH,'//input[@placeholder="Password"]')
    password.send_keys(pas)

    button = driver.find_element(By.XPATH,'//button[ @ type = "submit"]')
    button.click()
    WebDriverWait(driver, 10).until(EC.staleness_of(button))
    try:
        element = WebDriverWait(driver,5).until(
            EC.presence_of_element_located((By.XPATH, '//p[contains(@class,"oxd-alert-content-text")]'))
        )
        message = driver.find_element(By.XPATH,'//p[contains(@class,"oxd-alert-content-text")]')
        print(message.text)
    except Exception as e:
       pass
    time.sleep(3)

def close_driver(driver):
    driver.quit()
def del_emp(driver,id):
    driver.find_element(By.XPATH, '//a[@href ="/web/index.php/pim/viewPimModule"]').click()
    time.sleep(5)
    while True :
        try:
            driver.find_element(By.XPATH,f'//div[contains(@class,"clickable")]//div[contains(.,"{id}") and @class]/../div[last()]/div/button[1]').click()
            time.sleep(4)
            driver.find_element(By.XPATH,'//button[contains(.," Yes, Delete ")]').click()
            time.sleep(4)
            print("Deleted successfully")
            ,  except:
            driver.find_element(By.XPATH,'//button[contains(@class,"-page-item--previous-next")]').click()
            time.sleep(3)

def main():
    driver = launch_browser('chrome')
    login(driver,"Admin","admin123")
    # edit_employee(driver,id,middle)
    del_emp(driver,"0087")
    close_driver(driver)
main()
