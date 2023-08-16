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
    admin = driver.find_element(By.XPATH, '//ul[@class="oxd-main-menu"]/li/a[contains(@href, "viewAdmin")]')
    assert admin.text == "Admin"
    print("Admin is displayed on the admin page")

    # PIM
    pim = driver.find_element(By.XPATH, '//ul[@class="oxd-main-menu"]/li/a[contains(@href, "viewPimModule")]')
    assert pim.text == "PIM"
    print("PIM is displayed on the admin page")

    # Leave
    leave = driver.find_element(By.XPATH, '//ul[@class="oxd-main-menu"]/li/a[contains(@href, "viewLeaveModule")]')
    assert leave.text == "Leave"
    print("Leave is displayed on the admin page")

    # Time
    _time = driver.find_element(By.XPATH, '//ul[@class="oxd-main-menu"]/li/a[contains(@href, "viewTimeModule")]')
    assert _time.text == "Time"
    print("Time is displayed on the admin page")

    # Recruitment
    recruitment = driver.find_element(By.XPATH,
                                      '//ul[@class="oxd-main-menu"]/li/a[contains(@href, "viewRecruitmentModule")]')
    assert recruitment.text == "Recruitment"
    print("Recruitment is displayed on the admin page")

    # My Info
    my_info = driver.find_element(By.XPATH, '//ul[@class="oxd-main-menu"]/li/a[contains(@href, "viewMyDetails")]')
    assert my_info.text == "My Info"
    print("My Info is displayed on the admin page")

    # Performance
    performance = driver.find_element(By.XPATH,
                                      '//ul[@class="oxd-main-menu"]/li/a[contains(@href, "viewPerformanceModule")]')
    assert performance.text == "Performance"

    # Dashboard
    dashboard = driver.find_element(By.XPATH, '//ul[@class="oxd-main-menu"]/li/a[contains(@href, "dashboard")]')
    assert dashboard.text == "Dashboard"
    print("Dashboard is displayed on the admin page")

    # Directory
    directory = driver.find_element(By.XPATH, '//ul[@class="oxd-main-menu"]/li/a[contains(@href, "viewDirectory")]')
    assert directory.text == "Directory"
    print("Directory is displayed on the admin page")

    # Maintenance
    maintenance = driver.find_element(By.XPATH,
                                      '//ul[@class="oxd-main-menu"]/li/a[contains(@href, "viewMaintenanceModule")]')
    assert maintenance.text == "Maintenance"
    print("Maintenance is displayed on the admin page")

    # Buzz
    buzz = driver.find_element(By.XPATH, '//ul[@class="oxd-main-menu"]/li/a[contains(@href, "viewBuzz")]')
    assert buzz.text == "Buzz"
    print("Buzz is displayed on the admin page")


def close_driver(driver):
    driver.quit()


def main():
    driver = launch_browser('chrome')
    login(driver,"Admin","admin123")

    close_driver(driver)
main()
