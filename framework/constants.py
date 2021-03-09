import os
from config import TOOL_PATH


class Script:
    CLEAR_DATA = os.path.join(TOOL_PATH, "scripts", "clear_data.sh")
    CLEAR_LOGS = os.path.join(TOOL_PATH, "scripts", "clear_logs.sh")
    GET_PROCESS_ID = os.path.join(TOOL_PATH, "scripts", "get_process_id.sh")
    GET_COVERAGE = os.path.join(TOOL_PATH, "scripts", "retrieve_coverage.sh")
    GET_LOGS = os.path.join(TOOL_PATH, "scripts", "retrieve_logs.sh")
    CHANGE_LANDSCAPE = os.path.join(TOOL_PATH, "scripts", "change_landscape.sh")
    CHANGE_PORTRAIT = os.path.join(TOOL_PATH, "scripts", "change_portrait.sh")
    POWER_ON = os.path.join(TOOL_PATH, "scripts", "power_on.sh")
    POWER_OFF = os.path.join(TOOL_PATH, "scripts", "power_off.sh")
    SET_BATTERY_HIGH = os.path.join(TOOL_PATH, "scripts", "set_battery_high.sh")
    SET_BATTERY_LOW = os.path.join(TOOL_PATH, "scripts", "set_battery_low.sh")
    INTERNET_CONNECTED = os.path.join(TOOL_PATH, "scripts", "internet_connected.sh")
    INTERNET_DISCONNECTED = os.path.join(TOOL_PATH, "scripts", "internet_disconnected.sh")
