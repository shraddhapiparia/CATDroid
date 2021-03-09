import logging
import random
import time
import config
#from config import ADB_PATH

from constants import GUIActionType, ContextActionType
from framework.utils import adb

logger = logging.getLogger(__name__)


class Executor:
    def __init__(self, driver, event_interval, text_values):
        self.driver = driver
        self.event_interval = event_interval
        self.text_values = text_values

    def execute(self, event):
        actions = event["actions"]
        for action in actions:
            if action.action_type == GUIActionType.TEXT_ENTRY:
                selected_text_value = random.choice(self.text_values)
                action.value = selected_text_value

            action.execute(self.driver)

        time.sleep(self.event_interval)

    def executeContext(self, event):
        adbpath = config.ADB_PATH
        if event == "CHANGE_PORTRAIT":
            adb.change_portrait(adbpath)
        if event == "CHANGE_LANDSCAPE":
            adb.change_landscape(adbpath)
        if event == "POWER_ON":
            adb.power_on(adbpath)
        if event == "POWER_OFF":
            adb.power_off(adbpath)
        if event == "INTERNET_CONNECTED":
            adb.internet_connected(adbpath)
        if event == "INTERNET_DISCONNECTED":
            adb.internet_disconnected(adbpath)
        if event == "BATTERY_LOW":
            adb.battery_low(adbpath)
        if event == "BATTERY_HIGH":
            adb.battery_high(adbpath)

        time.sleep(self.event_interval)
