#!/usr/bin/python3
'''This script will take the gamelist xml file and sytem name and
create an updated xml gamelist and a scipt to rename files to  new filenames'''
import parse_xml as pxml
import sys

system_name = "NoSystemDefined"
#read the system name from the command line
print(f"Script name: {sys.argv[0]}")
if len(sys.argv) > 1:
    system_name = sys.argv[1]
    print(f"Processing for system: {system_name}\n")
else:
    print("system name needs to be used")
    exit

xml_file = pxml.XML_DIR + "gamelist_" + system_name + ".xml"
print(f"Using XML file: {xml_file}\n")

pxml.fixgamelist(xml_file,system_name)
print(f"Games from {xml_file} are processed.\n")
