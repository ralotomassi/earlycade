'''This script will read the corresponding gamelist xml file from
the ../xml/ folder and make a text file listing the games'''
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

xml_file = "../xml/gamelist_" + system_name + ".xml"
print(f"Using XML file: {xml_file}\n")

pxml.listgames(xml_file)
print(f"Games from {xml_file} are listed.\n")