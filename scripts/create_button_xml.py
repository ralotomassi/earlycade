'''This script will read the corresponding gamelist xml file from
the ../xml/ folder and make a blank button configuration
for the associated system'''
import parse_xml as pxml
import xml.etree.ElementTree as et
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

#if the system name is "all" the create buttons for all systems
all_systems = []
if system_name == "all":
    all_systems = [
                   "mame",
                   "neogeo",
                   "fba",
                   "nes",
                   "sega32",
                   "atari",
                   "snes"
                   ]

    for iSystem in all_systems:
        print(f"Processing for system: {iSystem}\n")
        pxml.addButtonsFromSystem(iSystem)
else:
        pxml.addButtonsFromSystem(system_name)

