#!/usr/bin/python3
#script to read a list of files and then make
#add a button category for each of the games associated with the file

import parse_xml as pxml
import os

gamefile = open(os.environ["GAMETEXT_DIR"] + "djump.txt", 'r')
gamelist = gamefile.readlines()
gamefile.close()

config_name = "djump"
for igame in gamelist:
	#remove the "_buttons.zip"
	igame = igame.replace("_buttons.png",".zip")

	#use the game name and config name to update the config file
	#make the image name
	pxml.updateTagTextForGame("button_config.xml",igame.strip(),"config_type",config_name)

exit
