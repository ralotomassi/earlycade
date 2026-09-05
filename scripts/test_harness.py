#!/usr/bin/python3
'''This test harness is used to test updates and upgrades to
the earlycade scripts.  All tests should be in the file'''

import parse_xml as pxml
import xml.etree.ElementTree as et
import sys
import os

def testAddGamesToRoot():

	#make the button config file name
	button_config_xml = pxml.XML_DIR + "test_button_config.xml"

	#make the test file list
	filelist = [
                    ["testgame1.zip","The New Game"],
                    ["testgame2.zip","Another New Game"]
                   ]

	#get the root from the existing tree
	button_config = et.parse(button_config_xml)
	root = button_config.getroot()

	root = pxml.addGamesToRoot(root,filelist,"Test_System")
	#write to file
	tree = et.ElementTree(root)

	tree.write(button_config_xml, encoding="UTF-8", xml_declaration=True)
	print(f"The test button config  is updated.\n")


#testing Adding new games to button config
testAddGamesToRoot()
