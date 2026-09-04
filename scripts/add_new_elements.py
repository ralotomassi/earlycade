#!/usr/bin/python3
#script to create new xml element for the button config and add theme

import parse_xml as pxml
import os
import xml.etree.ElementTree as et

XML_DIR = os.environ["XML_DIR"]
#make the button configuration file
def addElement():
	pxml.addElementToButtonConfig("has34","no")
def addDirectionalToButtonConfig():
	#open the button config and add the element
	#read the gamelist
	button_config = et.parse(XML_DIR + "button_config.xml")

	theRoot = button_config.getroot()

	print(theRoot.tag)

	#get all the systems
	all_systems = theRoot.findall("system")

	for isystem in all_systems:

		#get all the games
		all_games = isystem.findall("game")

		#loop thru games and add element
		for igame in all_games:
			#get the directional tag for each game
			directional_element = igame.find("directional")
			directional_element.text=""

			continue

			#add the sub elements
			type_element = et.SubElement(directional_element,"type")
			type_element.text = "none"

			up_element = et.SubElement(directional_element,"up")
			up_element.text = ""

			down_element = et.SubElement(directional_element,"down")
			down_element.text = ""

			left_element = et.SubElement(directional_element,"left")
			left_element.text = ""

			right_element = et.SubElement(directional_element,"right")
			right_element.text = ""

			#updated_system = all_systems.append(addElement)
	
	button_config.write(XML_DIR + "button_config.xml", encoding='utf-8', xml_declaration=True)
	print(f"Updated {XML_DIR}button_config.xml")

#addDirectionalToButtonConfig()
buttons = [
	"Low punnch",
	"Low Kick",
	"Med Punch",
	"Med Kick",
	"high punch",
	"high kick"
]

joysticks = [
	"jump",
	"run",
	"back up",
	"duck"
]
#pxml.addGlobalButtonType(buttons,"mortal_kombat")
	#this routine will add a global button config type to the xml this is
	#specifically used for images with buttons only and no joystick image
	#joysticks = ["","","",""]
pxml.addDirectionalImageTypeToXML(joysticks,buttons,"mortal_kombat2","both")
exit()
