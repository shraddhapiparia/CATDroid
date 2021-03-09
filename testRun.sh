#!/bin/bash

function start_acvTool {
    acv install instr_com.simplemobiletools.notes.pro_68.apk
    acv start com.simplemobiletools.notes.pro
}

function start_appium {
    source ~/.nvm/nvm.sh && \
    source ~/.profile && \
    source ~/.bashrc && \
    nvm use node && \
    appium --log-level warn:debug > appium.log &
}

start_appium


