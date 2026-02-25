#!/usr/bin/bash

echo "This is a Test"
DISPLAY=192.168.1.218:0.1
export DISPLAY
./parse_xml.py
