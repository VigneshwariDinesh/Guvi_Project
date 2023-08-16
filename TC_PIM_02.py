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
    # //ul[@class="oxd-main-menu"]/li/a[contains(@href, "viewAdmin")]
    admin_button = driver.find_element(By.XPATH, '//ul[@class="oxd-main-menu"]/li/a[contains(@href, "viewAdmin")]')
    admin_button.click()
    WebDriverWait(driver, 10).until(EC.staleness_of(admin_button))
    time.sleep(3)

    # validate title of the page as "OrangeHRM"
    assert driver.title == "OrangeHRM"
    print("Title of the page is: " + driver.title)

    # validate the below options are displaying on the admin page
    # User Management
    # Job
    # Organization
    # Qualifications
    # Nationalities
    # Configuration
    # Corporate Branding

    # User Management
    user_management = driver.find_element(By.XPATH,
                                          '//nav[@role="navigation"]/ul/li/span[contains(text(), "User Management")]')
    assert user_management.text == "User Management"
    print("User Management is displayed on the admin page")

    # Job
    job = driver.find_element(By.XPATH, '//nav[@role="navigation"]/ul/li/span[contains(text(), "Job")]')

    assert job.text == "Job"
    print("Job is displayed on the admin page")

    # Organization
    organization = driver.find_element(By.XPATH,
                                       '//nav[@role="navigation"]/ul/li/span[contains(text(), "Organization")]')
    assert organization.text == "Organization"
    print("Organization is displayed on the admin page")

    # Qualifications
    qualifications = driver.find_element(By.XPATH,
                                         '//nav[@role="navigation"]/ul/li/span[contains(text(), "Qualifications")]')
    assert qualifications.text == "Qualifications"
    print("Qualifications is displayed on the admin page")

    # Nationalities
    nationalities = driver.find_element(By.XPATH,
                                        '//nav[@role="navigation"]/ul/li/a[contains(text(), "Nationalities")]')
    assert nationalities.text == "Nationalities"
    print("Nationalities is displayed on the admin page")

    # Configuration
    configuration = driver.find_element(By.XPATH,
                                        '//nav[@role="navigation"]/ul/li/span[contains(text(), "Configuration")]')
    assert configuration.text == "Configuration"
    print("Configuration is displayed on the admin page")

    # Corporate Branding
    corporate_branding = driver.find_element(By.XPATH,
                                             '//nav[@role="navigation"]/ul/li/a[contains(text(), "Corporate Branding")]')
    assert corporate_branding.text == "Corporate Branding"
    print("Corporate Branding is displayed on the admin page")




def close_driver(driver):
    driver.quit()


def main():
    driver = launch_browser('chrome')
    login(driver,"Admin","admin123")

    close_driver(driver)
main()
