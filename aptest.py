from appium import webdriver


desired_caps = {
    "platformName": "Android",
    "deviceName": "Android Emulator",
    'appPackage': 'org.tomdroid',
    'appActivity': 'org.tomdroid.ui.Tomdroid',
    "udid": "emulator-5554"
}

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
page_source = driver.page_source
print(page_source)