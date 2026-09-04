#!/usr/bin/python3
#script to look at two xml files and list the games in the 1st that's
#missing from the 2nd

import parse_xml as pxml
import sys

system_name = "NoSystemDefined"
#read the system name from the command line
print(f"Script name: {sys.argv[0]}")
if len(sys.argv) > 1:
	filename1 = sys.argv[1]
	filename2 = sys.argv[2]

	print(f"Comparing files: {filename1} and {filename2}\n")
else:
	print("Both gamelist XMLs should be used")
	exit

xml_name1 = pxml.XML_DIR + filename1
xml_name2 = pxml.XML_DIR + filename2

filelist1 = pxml.listgames(xml_name1)
print(f"Games from {filename1} are listed.\n")

#now loop thru the 1st file and check to see if those items
#are in the second file
for igame in filelist1:
	#strip the game name from the complete path
	#igame = pxml.removePath(igame)

	#now use the game name to search the second find
	#print(f"Searching for {igame} in {xml_name2}")
    igame = pxml.removePath(igame)
    isGameThere = pxml.findgame(igame,xml_name2)

    if (isGameThere != True):
        #pass
        print(f"{igame} is not there")
    #else:
    #    print(f"{igame} exists")

print("All games have been searched")
	



