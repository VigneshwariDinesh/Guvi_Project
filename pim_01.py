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

def add_employee(driver,first,middle,last,id,username,password,image):
    driver.find_element(By.XPATH,'//a[@href ="/web/index.php/pim/viewPimModule"]').click()
    time.sleep(5)
    driver.find_element(By.XPATH,'//button[contains(.,"Add")]').click()
    time.sleep(3)
    driver.find_element(By.NAME,"firstName").send_keys(first)
    driver.find_element(By.NAME, "middleName").send_keys(middle)
    driver.find_element(By.NAME, "lastName").send_keys(last)
    id_input = driver.find_element(By.XPATH,'//label[contains(.,"Employee Id")]/../../div[2]/input')
    for _ in range(20):
        id_input.send_keys(Keys.BACK_SPACE)
    id_input.send_keys(id)
    file_input = driver.find_element(By.CLASS_NAME,'oxd-file-input')
    file_input.send_keys(image)

    driver.find_element(By.XPATH,'//span[@class="oxd-switch-input oxd-switch-input--active --label-right"]').click()
    time.sleep(6)
    driver.find_element(By.XPATH,'//label[contains(.,"Username")]/../../div[2]/input').send_keys(username)
    driver.find_element(By.XPATH, '(//label[contains(.,"Password")]/../../div[2]/input)[1]').send_keys(password)
    driver.find_element(By.XPATH, '(//label[contains(.,"Password")]/../../div[2]/input)[2]').send_keys(password)
    time.sleep(6)
    driver.find_element(By.XPATH,'//button[@type="submit"]').click()
    time.sleep(5)
    print("User added successfully")
def main():
    driver = launch_browser('chrome')
    login(driver,"Admin","admin123")
    add_employee(driver,"vic","ky","n","123","vicky","Aa@1234567",r"C:\Users\vicky\OneDrive\Pictures\Screenshots\Screenshot 2023-03-02 135626.png")
    close_driver(driver)
main()
