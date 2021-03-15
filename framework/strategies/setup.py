from appium import webdriver
from framework.utils.adb import clear_sdcard_data, change_context


def standard(apk_path, adb_path, device_id):
    clear_sdcard_data(adb_path, device_id)    
    # Setting initial context as portrait, internet on, battery high and power connected
    change_context(adb_path, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1)
    driver = _get_driver(apk_path, device_id)
    return driver


def _get_driver(apk_path, device_id):
    desired_caps = {
        "platformName": "Android",
        "deviceName": "Android Emulator",
        "app": apk_path,
        "newCommandTimeout": 3600,
        "autoGrantPermissions": True,
        "fullReset": True,
        "disableWindowAnimation": True,
        "appWaitActivity": "*",
        "udid": device_id
    }

    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

    return driver
