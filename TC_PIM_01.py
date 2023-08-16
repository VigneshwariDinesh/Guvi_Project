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
def forgetpassword(driver):
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    time.sleep(5)
    forgot_password_link = driver.find_element(By.CLASS_NAME, "orangehrm-login-forgot-header")
    forgot_password_link.click()
    time.sleep(5)
    username_textbox = driver.find_element(By.NAME, "username")
    username_textbox.send_keys("DummyUsername")

    reset_password_button = driver.find_element(By.XPATH,
                                                '//button[@type="submit"]')
    reset_password_button.click()
    time.sleep(5)
    print("Reset password link sent successfully")

def close_driver(driver):
    driver.quit()


def main():
    driver = launch_browser('chrome')
    forgetpassword(driver)

    close_driver(driver)
main()
