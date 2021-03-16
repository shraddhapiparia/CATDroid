import logging
import subprocess
from framework.constants import *

logger = logging.getLogger(__name__)


def clear_sdcard_data(adb_path, device_id):
    clear_sdcard_cmd = "{} {} {}".format(Script.CLEAR_DATA, adb_path, device_id)
    subprocess.check_call(clear_sdcard_cmd, shell=True)
    # logger.info("Successfully cleared SD card data.")


def clear_logs(adb_path, device_id):
    clear_logs_cmd = "{} {} {}".format(Script.CLEAR_LOGS, adb_path, device_id)
    subprocess.check_call(clear_logs_cmd, shell=True)
    logger.info("Successfully cleared logs.")


def get_process_id(adb_path, package_name, device_id):
    process_id_cmd = "{} {} {} {}".format(Script.GET_PROCESS_ID, adb_path, package_name, device_id)
    process = subprocess.Popen(process_id_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, errors = process.communicate()
    process_id = output.decode("utf-8").strip()
    logger.info("Process id for {} is {}.".format(package_name, adb_path))
    return process_id


def get_coverage(adb_path, device_path, coverage_path, coverage_name, broadcast, device_id):
    get_coverage_cmd = "{} {} {} {} {} {} {}".format(Script.GET_COVERAGE, adb_path, device_path, coverage_path,
                                                     coverage_name, broadcast, device_id)
    subprocess.call(get_coverage_cmd, shell=True)
    logger.info("Successfully retrieved coverage file: {}.".format(coverage_name))


def get_logs(adb_path, log_file_path, process_id, device_id):
    get_logs_cmd = "{} {} {} {} {}".format(Script.GET_LOGS, adb_path, log_file_path, process_id, device_id)
    subprocess.call(get_logs_cmd, shell=True)
    logger.info("Successfully retrieved log file: {}".format(log_file_path))

# Added by Shraddha Piparia for Context actions
def change_context(adb_path, ch_landscape, ch_portrait, power_on, power_off, internet_on, internet_off, battery_1pc, battery_2pc, battery_5pc, battery_15pc, battery_ok, battery_high):
    change_context_cmd = "{} {} {} {} {} {} {} {} {} {} {} {} {}".format(Script.CHANGE_CONTEXT, adb_path, ch_landscape, ch_portrait, power_on, power_off, internet_on, internet_off, battery_1pc, battery_2pc, battery_5pc, battery_15pc, battery_ok, battery_high)
    subprocess.call(change_context_cmd, shell=True)
    printval = ""
    if ch_portrait:
        printval += " Potrait mode, "
    if ch_landscape:
        printval += " Lanscape mode, "
    if power_on:
        printval += " Power ON, "
    if power_off:
        printval += " Power OFF, "
    if internet_on:
        printval += " Internet ON, "
    if internet_off:
        printval += " Internet OFF, "
    if battery_1pc:
        printval += " Battery 1PC, "
    if battery_2pc:
        printval += " Battery 2PC, "
    if battery_5pc:
        printval += " Battery 5PC, "
    if battery_15pc:
        printval += " Battery 15PC, "
    if battery_ok:
        printval += " Battery OK, "
    if battery_high:
        printval += " Battery HIGH, "
    logger.info("Successfully changed context {}".format(printval))
