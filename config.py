# Android settings
ADB_PATH = "/home/UNT/sp0809/Android/Sdk/platform-tools/adb"

# Autodroid settings
OUTPUT_PATH = "/home/UNT/sp0809/git/autodroid/output"
TOOL_PATH = "/home/UNT/sp0809/git/autodroid"
EVENT_INTERVAL = 2
TEST_SETUP = "Standard"
EVENT_SELECTION_STRATEGY = "frequency_weighted"
CONTEXT_STRATEGY = "pairs_interleaved"
TERMINATION_CRITERION = "Probabilistic"
COMPLETION_CRITERION = "Time"
TEST_TEARDOWN = "Standard"
TEST_SUITE_LENGTH = 10  # only used if completion criterion is "Length"
TIME_BUDGET = 7200  # (in seconds) only used if completion criterion is "Time"
TERMINATION_PROBABILITY = 0.05  # only used when termination criterion is "probabilistic"
TEST_CASE_LENGTH = 20  # only used if termination criterion is "length"
STRINGS_PATH = "strings.txt"
COVERAGE_BROADCAST = "com.context.FINISH_TESTING"

# AUT settings
APK_PATH = "/home/UNT/sp0809/git/autodroid/apps/app-prod-debug.apk"
APP_PACKAGE_NAME = "com.greenaddress.abcore"
COVERAGE_FILE_PATH = "/mnt/sdcard/com.greenaddress.abcore"

# Device settings
DEVICE_ID = "emulator-5554"
