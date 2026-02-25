#!/usr/bin/python3
#script to read a list of files and then make
#a bash script to copy those files to another directory

import cv2
gamefile = open("mame_games.txt", 'r')
gamelist = gamefile.readlines()
gamefile.close()

system_name = "mame_libetro"
image_dir = "/home/pi/PieMarquee2/marquee/arcade/"
marquee_dir = "/home/pi/PieMarquee2/marquee/" + system_name + "/"
for igame in gamelist:
	#remove the "-image.jpg"
	igame = (igame.replace("-image.jpg","")).strip()
	#make the image name
	igame_image = igame + ".png"
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
		#now converth the image to the 4:3 format
		resized_image = cv2.resize(image,(1024,768))

		#now save the image in the other format
		did_save = cv2.imwrite(marquee_dir+igame_marquee,resized_image)

		#check the save
		if did_save:
			print(f"{igame_marquee} was saved successfully")
		else:
			print(f"{igame_marquee} failed to save")



exit
