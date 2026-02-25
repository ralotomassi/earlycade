#!/usr/bin/python3
#script to read a list of files and then make
#a bash script to copy those files to another directory

import cv2
import os
gamefile = open("mame_games.txt", 'r')
gamelist = gamefile.readlines()
gamefile.close()

system_name = "mame_libetro"
image_dir = "/home/pi/PieMarquee2/marquee/arcade/"
for igame in gamelist:
	#remove the "-image.jpg"
	igame = (igame.replace("-image.jpg","")).strip()
	igame = (igame.replace("-image.png","")).strip()
	#make the image name
	igame_image = igame + ".png"
	#print(f"{igame} {igame_image}")
	#check to see if file exists
	if not os.path.exists(image_dir+igame_image):
		print(f"{igame}")
exit
