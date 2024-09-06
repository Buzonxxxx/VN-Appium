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
    'appPackage': 'com.VCB',
    'appActivity': '.ui.activities.splash.SplashActivity',
}

driver = webdriver.Remote('http://localhost:4724', options=UiAutomator2Options().load_capabilities(capabilities))

try:
    allowButton = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((AppiumBy.ID, 'com.android.permissioncontroller:id/permission_allow_button'))
    )
    allowButton.click()
    
    input = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((AppiumBy.ID, 'com.VCB:id/llInput'))
    )
    input.click()
    time.sleep(2)
    driver.press_keycode(7)
    driver.press_keycode(8)
    driver.press_keycode(9)
    driver.press_keycode(10)
    driver.press_keycode(11)
    driver.press_keycode(12)
    driver.press_keycode(13)
    driver.press_keycode(14)
    driver.press_keycode(15)
    driver.press_keycode(16)
    driver.press_keycode(8)

except TimeoutException:
    print("Element not found or not clickable")

time.sleep(10)
driver.quit()