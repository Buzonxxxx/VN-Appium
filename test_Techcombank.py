import time
from appium import webdriver
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common import TimeoutException

capabilities = {
    'deviceName': 'Galaxy A5',
    'platformName': 'Android',
    'automationName': 'UiAutomator2',
    'platformVersion': '14.0',
    'appPackage': 'vn.com.techcombank.bb.app',
    'appActivity': 'com.techcombank.retail.MainActivity',
}

driver = webdriver.Remote('http://localhost:4724', options=UiAutomator2Options().load_capabilities(capabilities))

try:
    loginButton = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((AppiumBy.ID, 'vn.com.techcombank.bb.app:id/btnLogin'))
    )
    loginButton.click()

    title = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((AppiumBy.ID, 'vn.com.techcombank.bb.app:id/tvUserNameLabel'))
    )

    driver.find_element(by=AppiumBy.CLASS_NAME, value='android.widget.EditText').send_keys("Harry")
    driver.find_element(AppiumBy.ID, 'vn.com.techcombank.bb.app:id/btnContinue').click()

except TimeoutException:
    print("Element not found or not clickable")

time.sleep(10)
driver.quit()