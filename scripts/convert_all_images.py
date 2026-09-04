#!/usr/bin/python3
#script to go thru all games and convert to 4:3 images and 
#save in correct PieMarquee2 locations

import cv2
import xml.etree.ElementTree as et
import os

def convertMarquee(from_image,to_image):
        image = cv2.imread(from_image)
        if image is None:
                print(f"Error getting {from_image}\n")
        else:
                print(f"{from_image} loaded successfully")
                #now converth the image to the 4:3 format
                resized_image = cv2.resize(image,(1024,768))

                #now save the image in the other format
                did_save = cv2.imwrite(to_image,resized_image)

                #check the save
                if did_save:
                        print(f"{to_image} was saved successfully")
                else:
                        print(f"{to_image} failed to save")



#build the list of folders
listSystem = list()
listSystem.append("atari2600")
listSystem.append("atari5200")
listSystem.append("fba")
listSystem.append("mastersystem")
listSystem.append("megadrive")
listSystem.append("nes")
listSystem.append("snes")
listSystem.append("sega32x")

#marquee_dir = "/home/pi/PieMarquee2/marquee/"

def convertAllSystemImages(system_name,target_dir):
        #read the gamelist
        gamelist_dir = GAMELIST_DIR + system_name +"/"
        gamelist_xml = gamelist_dir + "gamelist.xml"
        gamelist = et.parse(gamelist_xml)

        theRoot = gamelist.getroot()

        #loop thru each game and convert
        for game in theRoot.findall('game'):
                path_and_filename = game.find('path').text
                path_and_name = path_and_filename.replace(".zip","")
                filename = path_and_name.replace("./","")
                #print(filename)
                image = game.find('image')
                if image is not None:
                        from_image = image.text
                        from_image = from_image.replace("~/","/home/pi/")
                        to_image = target_dir + "/" + filename + ".png"
                        print(f"Converting {from_image} to\n {to_image}")
                        convertMarquee(from_image,to_image)
                else:
                        image_text = "No image"

for system in listSystem:
	#make the target directory 
	system_marquee_dir = PIEMARQUEE_DIR + system
	if not os.path.exists(system_marquee_dir):
		os.mkdir(system_marquee_dir)
		print(f"Created {system_marquee_dir}")
	else:
		print(f"{system_marquee_dir} already exists")

	#read the gamelist file and get each game
	convertAllSystemImages(system,system_marquee_dir)
	gamelist_dir = GAMELIST_DIR + system +"/"
	convertAllSystemImages(system,system_marquee_dir)

#for igame in gamelist:
#	#remove the .zip
#	igame = (igame.replace(".zip","")).strip()
#	#make the image name
#	igame_image = igame + "-image.jpg"
#	#make the marquee file
#	igame_marquee = igame + ".png"
#	print(f"{igame} {igame_image} {igame_marquee}")
#	#open the image
#	image = cv2.imread(image_dir+igame_image)

#	#check the image
#	if image is None:
#		print(f"Error getting {igame_image}\n")
#	else:
#		print(f"{igame_image} loaded successfully")
#		#now save the image in the other format
#		did_save = cv2.imwrite(marquee_dir+igame_marquee,image)
#
#		#check the save
#		if did_save:
#			print(f"{igame_marquee} was saved successfully")
#		else:
#			print(f"{igame_marquee} failed to save")



exit
