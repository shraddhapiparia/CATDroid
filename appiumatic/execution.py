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

    def execute_context(self, ch_landscape, ch_portrait, power_on, power_off, internet_on, internet_off, battery_1pc, battery_2pc, battery_5pc, battery_15pc, battery_ok, battery_high):
        adbpath = config.ADB_PATH
        adb.change_context(adbpath, ch_landscape, ch_portrait, power_on, power_off, internet_on, internet_off, battery_1pc, battery_2pc, battery_5pc, battery_15pc, battery_ok, battery_high)

        time.sleep(self.event_interval)
