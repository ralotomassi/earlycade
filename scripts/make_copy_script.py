#!/usr/bin/python3
#script to read a list of files and then make
#a bash script to copy those files to another directory

import cv2
import os 
gamefile = open("neogeo_games.txt", 'r')
gamelist = gamefile.readlines()
gamefile.close()

system_name = "neogeo"
image_dir = os.environ["IMAGE_DIR"] + system_name +"/"
marquee_dir = os.environ["PIEMARQUEE_DIR"] + system_name + "/"
for igame in gamelist:
	#remove the .zip
	igame = (igame.replace(".zip","")).strip()
	#make the image name
	igame_image = igame + "-image.jpg"
	#make the marquee file
	igame_marquee = igame + ".png"
	print(f"{igame} {igame_image} {igame_marquee}")
	#open the image
	image = cv2.imread(image_dir+igame_image)

	#check the image
	if image is None:
		print(f"Error getting {igame_image}\n")
	else:
		print(f"{igame_image} loaded successfully")
		#now save the image in the other format
		did_save = cv2.imwrite(marquee_dir+igame_marquee,image)

		#check the save
		if did_save:
			print(f"{igame_marquee} was saved successfully")
		else:
			print(f"{igame_marquee} failed to save")

exit
