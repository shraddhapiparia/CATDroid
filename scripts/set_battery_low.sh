#!/bin/bash

ADB_PATH=$1
#echo "ADB PATH at script is : $ADB_PATH"
$ADB_PATH shell dumpsys battery set level 5 # Battery very low
