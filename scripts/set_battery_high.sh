#!/bin/bash
ADB_PATH=$1

$ADB_PATH shell dumpsys battery reset
