#!/bin/bash

# change to landscape

ADB_PATH=$1

$ADB_PATH shell content insert --uri content://settings/system --bind name:s:accelerometer_rotation --bind value:i:0
$ADB_PATH shell content insert --uri content://settings/system --bind name:s:user_rotation --bind value:i:0
