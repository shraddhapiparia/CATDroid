#!/bin/bash

# Get all parameters
ADB_PATH=$1
CH_LANDSCAPE=$2
CH_PORTRAIT=$3
POWER_ON=$4
POWER_OFF=$5
INTERNET_CONNECTED=$6
INTERNET_DISCONNECTED=$7
BATTERY_1PC=$8
BATTERY_2PC=$9
BATTERY_5PC=$10
BATTERY_15PC=$11
BATTERY_OK=$12
BATTERY_HIGH=$13

# change to landscape
if [ CH_LANDSCAPE ]
then
  $ADB_PATH shell content insert --uri content://settings/system --bind name:s:accelerometer_rotation --bind value:i:0
  $ADB_PATH shell content insert --uri content://settings/system --bind name:s:user_rotation --bind value:i:1
fi

# Change to portrait
if [ CH_PORTRAIT ]
then
  $ADB_PATH shell content insert --uri content://settings/system --bind name:s:accelerometer_rotation --bind value:i:0
  $ADB_PATH  shell content insert --uri content://settings/system --bind name:s:user_rotation --bind value:i:0
fi

# power off
if [ POWER_OFF ]
then
  $ADB_PATH shell dumpsys battery set ac 0
  $ADB_PATH shell settings put global heads_up_notifications_enabled 0
fi

# power on
if [ POWER_ON ]
then
  $ADB_PATH shell dumpsys battery set ac 1
fi

# Internet disable
if [ INTERNET_DISCONNECTED ]
then
  $ADB_PATH shell svc wifi disable
  $ADB_PATH shell svc data disable
fi

# Internet enable
if [ INTERNET_CONNECTED ]
then
  $ADB_PATH shell svc wifi enable
  $ADB_PATH shell svc data enable
fi

# Battery high
if [ BATTERY_HIGH ]
then
  $ADB_PATH shell dumpsys battery reset
fi

# Battery 1pc
if [ BATTERY_1PC ]
then
  $ADB_PATH shell dumpsys battery set level 1
fi

# Battery 2pc
if [ BATTERY_2PC ]
then
  $ADB_PATH shell dumpsys battery set level 2
fi

# Battery 5pc
if [ BATTERY_5PC ]
then
  $ADB_PATH shell dumpsys battery set level 5
fi

# Battery 15pc
if [ BATTERY_15PC ]
then
  $ADB_PATH shell dumpsys battery set level 15
fi

# Battery ok
if [ BATTERY_OK ]
then
  $ADB_PATH shell dumpsys battery set level 65
fi
