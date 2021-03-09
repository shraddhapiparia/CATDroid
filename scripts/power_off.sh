#!/bin/bash

ADB_PATH=$1
$ADB_PATH shell dumpsys battery set ac 0
$ADB_PATH shell settings put global heads_up_notifications_enabled 0
