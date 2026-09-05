#!/usr/bin/python3
#script to read a list of files and then make
#a bash script to copy those files to another directory

import cv2
import xml.etree.ElementTree as et
import os

#constants
MEDIA_DIR = os.environ["MEDIA_DIR"]
INSTRUCTION_DIR = os.environ["INSTRUCTION_DIR"]
PIEMARQUEE_DIR= os.environ["PIEMARQUEE_DIR"]
CUSTOM_DIR = os.environ["CUSTOM_DIR"]
XML_DIR = os.environ["XML_DIR"]
GAMELIST_DIR = os.environ["GAMELIST_DIR"]
NONE = 0
HORIZONTAL = 1
VERTICAL  = 2
BOTH = 3


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

def fixname(oldname):
	newname = ""
    #remove parens and everything inside
	x =0
	while oldname.find("(") > -1:
		x = x+1
		#print(oldname)
		startpos = oldname.find("(")
		endpos = oldname.find(")")
		removetext = oldname[startpos:endpos + 1]
		oldname = oldname.replace(removetext,"")
		newname = oldname
		if x == 10:
			break
	#remove trailing or ending spaces
	thesplit = oldname.split(".zip")
	basename = (thesplit[0]).strip()
	basename = basename.lower()
	basename = basename.replace(" ","_")
	basename = basename.replace(".","")
	basename = basename.replace("+","")
	basename = basename.replace("'","")
	basename = basename.replace(",","_")
	basename = basename.replace("-","")
	basename = basename.replace("___","_")
	basename = basename.replace("__","_")
	newname = basename
	
	return(newname)

def getzipname(fullpath):
	startpos = fullpath.rfind('/')
	endpos = fullpath.find(".zip")
	basename = fullpath[startpos+1:endpos]
	print(basename)
	return(basename)

def makeMarqueeWithCategory(button_category,gamename,system_name):
	#remove the zip from the game name
	gamename = gamename.replace(".zip","")
	#instruction_path = "/home/pi/PieMarquee2/marquee/instruction/"
	marquee_path = PIEMARQUEE_DIR + system_name + "/"

	#instruction line
	instruct_line = INSTRUCTION_DIR  + button_category + ".png"
	
	#marquee line
	marquee_line = marquee_path + gamename + ".png"

	custom_file_name = os.environ["CUSTOM_DIR"] + gamename + ".txt"
	custom_file = open(custom_file_name,'w')
	custom_file.write(instruct_line + '\n')
	custom_file.write(marquee_line + '\n')
	custom_file.close()

def createCustomMarquee(gamename,system_name,button_category = "none"):
	#remove the zip from the game name
	gamename = gamename.replace(".zip","")
	marquee_path = PIEMARQUEE_DIR + system_name + "/"
	
	#use the category if it exists
	if button_category == "none":
		#instruction line
		instruct_line = INSTRUCTION_DIR  + gamename + "_buttons.png"
	else:
		#instruction line
		instruct_line = INSTRUCTION_DIR  + button_category + ".png"

	#marquee line
	marquee_line = marquee_path + gamename + ".png"

	custom_file_name = CUSTOM_DIR + gamename + ".txt"
	custom_file = open(custom_file_name,'w')
	custom_file.write(marquee_line + '\n')
	custom_file.write(instruct_line + '\n')
	custom_file.write(INSTRUCTION_DIR  + "gameexit.png"  + '\n')
	custom_file.close()

def replaceElementText(parent,child,new_text):
	#rename line is the line in the move script to update actual file name
	rename_line = ""

	#attemp to get the child element
	element = parent.find(child)
	if element is None:
		print(f"No tag exists.  Adding tag\n")
		old_text = "NONE"
		new_element = et.SubElement(parent,child)
		new_element.text = new_text
	elif element.text == "":
		print(f"Text is blank\n")
		element.text = new_text
	elif element.text is None:
		print(f"Text is None.  Adding text\n")
		element.text = new_text
	else:
		old_text = element.text
		element.text = new_text
		rename_line = 'mv "' + old_text + '"' + ' ' + new_text + '\n'
	return(parent,rename_line)


def fixgamelist(xmlfile,system_name):

	#open file to hold bash mv commands
	mvscript = open("move_" + system_name + "_files.sh",'w')
	mvscript.write("#!/usr/bin/bash\n")

	#read the gamelist
	gamelist = et.parse(xmlfile)

	theRoot = gamelist.getroot()

	print(theRoot.tag)

	numgames = 0

	old_image = ""
	old_marquee = ""
	old_path = ""
	old_video = ""
	for igame in theRoot.findall('game'): #findall() gets all direct children with the tag 'game'
		numgames += 1
		path = igame.find('path')
		oldname = getzipname(path.text)
		print(path.text)
		newname = fixname(oldname)

		image_dir = MEDIA_DIR + system_name + "/screenshots/"
		new_element = replaceElementText(igame,"image",image_dir + newname + ".png")
		igame = new_element[0]
		mvscript.write( new_element[1])

		marquee_dir = MEDIA_DIR + system_name + "/marquees/"
		new_element = replaceElementText(igame,"marquee",marquee_dir + newname + ".png")
		igame = new_element[0]
		mvscript.write( new_element[1])
		
		video_dir = MEDIA_DIR + system_name + "/videos/"
		new_element = replaceElementText(igame,"video",video_dir + newname + ".mp4")
		igame = new_element[0]
		mvscript.write( new_element[1])

		#create line to rename the marquees
		piemarquee_dir = PIEMARQUEE_DIR + system_name + "/"
		mvscript.write('mv "' + piemarquee_dir + oldname + '.png"' + ' ' + piemarquee_dir + newname + '.png\n')
		
		print (newname + '\n')
		old_path = path.text
		path.text = (path.text).replace(oldname,newname)
		
		#add the new element
		button_element = et.SubElement(igame,"button_config")
		button_element.text = newname + "_buttons.png"

		#write line to move zip file
		mvscript.write('mv "' + old_path + '"' + ' ' + path.text + '\n\n')

	mvscript.close()
	updated_xml_path = xmlfile.replace(".xml","_updated.xml")
	gamelist.write(updated_xml_path, encoding="UTF-8", xml_declaration=True)

def listgames(xml_file_name):

	#open file to list the games
	file_list_name = xml_file_name.replace(".xml",".txt")
	file_list_name = file_list_name.replace("/xml/","/gametext/")
	file_list = open(file_list_name,'w')

	#read the gamelist
	gamelist = et.parse(xml_file_name)

	theRoot = gamelist.getroot()

	print(theRoot.tag)

	#get all the games
	allgames = theRoot.findall('game') #findall() gets all direct children with the tag 'game'
	numgames = len(allgames)
	file_list.write(f"# {numgames}\n")
	pathlist = list()
	for igame in allgames: 
		name = igame.find('name')
		gamename = name.text
		file_list.write(gamename + '\n')

		#add the game file to a list
		path = igame.find("path")
		pathlist.append(path.text)

		print(gamename + "     " + path.text)
		
	file_list.close()
	print(f"Games have been written to {file_list_name}")
	return(pathlist)

def removePath(pathAndFile):
	pos = pathAndFile.rfind("/")
	fileName = pathAndFile[pos + 1:]
	return(fileName)

def addButtonConfigurationToElement(root,buttons):
	
	print(f"Adding buttons for global configuration")
	buttona = et.SubElement(root,"a_config")
	buttona.text = buttons[0]

	buttonb = et.SubElement(root,"b_config")
	buttonb.text = buttons[1]

	buttonx = et.SubElement(root,"x_config")
	buttonx.text = buttons[2]

	buttony = et.SubElement(root,"y_config")
	buttony.text = buttons[3]

	buttonl = et.SubElement(root,"l_config")
	buttonl.text = buttons[4]

	buttonr = et.SubElement(root,"r_config")
	buttonr.text = buttons[5]

	return(root)

def addDirectionalConfigToElement(root,joysticks,direction):

	print(f"Adding joysticks for global configuration")
	#add the directional tag 
	directional_element = et.SubElement(root,"directional")

	#add the sub elements
	type_element = et.SubElement(directional_element,"type")
	type_element.text = direction

	up_element = et.SubElement(directional_element,"up")
	up_element.text =joysticks[0]

	down_element = et.SubElement(directional_element,"right")
	down_element.text = joysticks[1]

	left_element = et.SubElement(directional_element,"down")
	left_element.text = joysticks[2]

	right_element = et.SubElement(directional_element,"left")
	right_element.text = joysticks[3]

	return root

def addDirectionalImageTypeToXML(joysticks,buttons,typename,direction):
	#this routine takes the passed parameters and adds a directional instruction
	#image to the global type xml file
	
	#open the image type configuration xml and parse the tree
	config_file_name = XML_DIR + "global_button_config.xml"
	button_config = et.parse(config_file_name)

	#get the root element
	theRoot = button_config.getroot()

	print(f"Adding config type to global configuration")
	configuration_element = et.SubElement(theRoot,"configuration") 
	global_config_name = et.SubElement(configuration_element,"typename")
	global_config_name.text = typename
	
	#add the button configuration to the element
	configuration_element = addButtonConfigurationToElement(configuration_element,buttons)

	#if necassary, add the directional information to element
	if (direction != "none"):
		configuration_element = addDirectionalConfigToElement(configuration_element,joysticks,direction)

	custom_file_created_element = et.SubElement(configuration_element,"custom_file_created")
	custom_file_created_element.text = "false"

	#save the new file
	tree = et.ElementTree(theRoot)
	tree.write(XML_DIR + "global_button_config.xml", encoding='utf-8', xml_declaration=True)
	print(f"Udated {XML_DIR}{config_file_name}")

def addGlobalButtonType(buttons,typename):
	#this routine will add a global button config type to the xml this is
	#specifically used for images with buttons only and no joystick image
	joysticks = ["","","",""]
	root = addDirectionalImageTypeToXML(joysticks,buttons,typename,"none")

def addGamesToRoot(root,filelist,system_name):
	numgames = len(filelist)

	#add the system if it doesn't already exist
	#system_element = root.find(system_name)
	system_element = root.find(f".//system[@systemname='{system_name}']")
	if  system_element is None:
		print(f"System {system_name} is not already there.")
		attributes = {
			         'systemname': system_name,
			         'count': str(numgames)
			         }

		# Create the element with multiple attributes directly
		# The attributes dictionary is passed as keyword arguments
		system_element = et.SubElement(root,"system",attrib = attributes)
		
	for igame in filelist:
		zipname = removePath(igame[0])
		game_title = igame[1]
		
		# The XPath expression is .//tagname[@attribute_name='attribute_value']
		element = root.find(f".//game[@filename='{zipname}']")

		if element is not None:
			print(f"{zipname} already is there")
		else:
			print(f"Adding {zipname} to button configuration")
			game_element = et.SubElement(system_element,"game", filename = zipname)
			name_element = et.SubElement(game_element,"name")
			name_element.text = game_title

			#set up the default button values
			buttons = [
				"off",
				"off",
				"off",
				"off",
				"off",
				"off"
			]

			#add the button configuration to the element
			game_element = addButtonConfigurationToElement(game_element,buttons)

			buttonConfigType = et.SubElement(game_element,"config_type")
			buttonConfigType.text = "none"

			joysticks = [
							"",
							"",
							"",
							""
						]
			game_element = addDirectionalConfigToElement(game_element,joysticks,"none")

			buttonConfigType = et.SubElement(game_element,"image")
			buttonConfigType.text = "none"

			buttonConfigType = et.SubElement(game_element,"custom_file_created")
			buttonConfigType.text = "false"

	return(root)

def addElementToButtonConfig(newElement,newValue = "none"):
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
			addElement = et.SubElement(igame,newElement)
			addElement.text = newValue
			updated_system = all_systems.append(addElement)
	
	button_config.write(XML_DIR + "button_config.xml", encoding='utf-8', xml_declaration=True)
	print(f"Updated {XML_DIR}button_config.xml")

def formatNewXml(button_config_xml,system_name):

	system_tag = "<" + system_name + ">"
	#format the xml
	xmlfile = open(button_config_xml,'r')
	xmltext = xmlfile.read()
	xmltext = xmltext.replace('.zip">','.zip">\n\t\t')
	xmltext = xmltext.replace("<Button_Config>","<Button_Config>\n")
	xmltext = xmltext.replace(system_tag,system_tag + "\n\t")
	xmltext = xmltext.replace("><game>",">\n\t<game>")
	xmltext = xmltext.replace("<game>","<game>\n\t\t")
	xmltext = xmltext.replace("/game>","/game>\n\t")
	xmltext = xmltext.replace("/name>","/name>\n\t\t")
	xmltext = xmltext.replace("/a_config>","/a_config>\n\t\t")
	xmltext = xmltext.replace("/b_config>","/b_config>\n\t\t")
	xmltext = xmltext.replace("/x_config>","/x_config>\n\t\t")
	xmltext = xmltext.replace("/y_config>","/y_config>\n\t\t")
	xmltext = xmltext.replace("/l_config>","/l_config>\n\t\t")
	xmltext = xmltext.replace("/r_config>","/r_config>\n\t\t")
	xmltext = xmltext.replace("/config_type>","/config_type>\n\t")
	xmltext = xmltext.replace("\n\t\t\n","\n")
	xmltext = xmltext.replace("\n\t\n","\n")
	xmltext = xmltext.replace("\n\n","\n")

	xmlfile.close()

	xmlfile = open(button_config_xml,'w')
	xmlfile.write(xmltext)
	xmlfile.close()

	exit

def getSystemElements(xml_file):
	#open the config file and get all the "system" elements
	button_config = et.parse(xml_file)

	theRoot = button_config.getroot()
	
	print(theRoot.tag)

	#get all the systems
	all_systems = theRoot.findall(".//system")

	return(all_systems)

def getGameElements(xml_file):
	#open the button config and add the element
	#read the gamelist
	button_config = et.parse(xml_file)

	theRoot = button_config.getroot()

	print(theRoot.tag)

	#get all the games
	all_games = theRoot.findall(".//game")

	return(all_games)

def getTextGamelist(xml_file):
	gamelist = list()
	game_elements = getGameElements(xml_file)
	for igame in game_elements:
		path_element = igame.find("path")
		name_element = igame.find('name')
		gamelist.append([path_element.text, name_element.text])
	return(gamelist)

def addButtonsFromSystem(system_name):
    xml_file = XML_DIR + "gamelist_" + system_name + ".xml"
    print(f"Using XML file: {xml_file}")

	#make the button config file name
    button_config_xml = XML_DIR + "button_config.xml"

    #get the file list from the xml
    filelist = getTextGamelist(xml_file)

    import os
    # check to see if button config already exist
    if os.path.isfile(button_config_xml):
        print(f"Button Config exist.  Appending new data to\n{button_config_xml}")

        #get the root from the existing tree
        button_config = et.parse(button_config_xml)
        root = button_config.getroot()
    else:
        print(f"Creating new button config")

        #make the button configuration file
        root = et.Element("Button_Config")

    root = addGamesToRoot(root,filelist,system_name)
    #write to file
    tree = et.ElementTree(root)

    tree.write(button_config_xml, encoding="UTF-8", xml_declaration=True)
    #format the new xml
    formatNewXml(button_config_xml,system_name)
    print(f"Blank button Config for {system_name} is created.\n")

def updateTagTextForGame(btn_cfg, gameName, tag, newText):
	#this routine will search the xml file that has the button_xml format
	#for the [gameName] and change the [tag] value to [newText]
	
	#open the button config and add the new text
	#read the gamelist
    button_config = et.parse(XML_DIR + btn_cfg)

    theRoot = button_config.getroot()

    print(theRoot.tag)

	#get the element with filename = gamename
	#search recursively("//") for all games with filename attribute equal to gameName
    findString = ".//game[@filename='" + gameName + "']"
    print(f"The find string is {findString}")
    element = theRoot.find(findString)

    #add the [newText] to the [tag]
    tagElement = element.find(tag)
    tagElement.text = newText
        
    button_config.write(XML_DIR + btn_cfg, encoding='utf-8', xml_declaration=True)
    print(f"Added {newText} to {tag} for {gameName}")

def findgame(game_zip_name,xml_file):
	#this routine will search the xml file for the game zip name
    #because the paths may vary, this routine will strip the path names
    #and do a brute force search
	#print(f"parsing xml file {xml_file}")
    
    #strip the path from the passed game name 
    game_to_search_for = removePath(game_zip_name)
    
    gamesdb = et.parse(xml_file)
    theRoot = gamesdb.getroot()
    
    #get all the games
    allgames = theRoot.findall('game') #findall() gets all direct children with the tag 'game'
    numgames = len(allgames)

    found_game = False
    for igame in allgames: 
        #add the game file to a list
        path = igame.find("path")
        zip_name = removePath(path.text)
        
        #compare the names
        if (game_to_search_for == zip_name):
            found_game = True 

    return found_game


