'''This script will read the corresponding button configuration xml file from
the ../xml/ folder and make the button instruction images and then also create
the custom marquee text file.  It places the buttons in a directory that is
../instruction/ and places the custom scripts in ../custom/ folder.'''

import parse_xml as pxml
import make_button_template as mbt
import xml.etree.ElementTree as et
import sys

system_name = "NoSystemDefined"
#read the system name from the command line
print(f"Script name: {sys.argv[0]}")
#if len(sys.argv) > 1:
#    system_name = sys.argv[1]
#    print(f"Processing for system: {system_name}\n")
#else:
#    print("system name needs to be used")
#    exit

xml_file = "../xml/button_config.xml"
print(f"Using XML file: {xml_file}\n")

#get all the system elements
systems = pxml.getSystemElements(xml_file)

for isystem in systems:
    system_name = isystem.attrib["systemname"]
    games = isystem.findall('game')
    print(f"Found {len(games)} games in {system_name}")

    #go thru each game element and make the buttons and then create the 
    #custom text file with the marquee and button image
    for igame in games:
        #get the game name
        gamename = igame.attrib['filename']

        #check to see if this is part of a category
        button_category = (igame.find("config_type")).text
        if (button_category != "none"):
            pxml.createCustomMarquee(gamename,system_name,button_category)
        else:
            #gamename = ((igame.find("name")).text).replace(".zip","")
            print(f"Makeing button image for {gamename}")

            #get each of the button configs
            a_function = (igame.find("a_config")).text
            b_function = (igame.find("b_config")).text
            x_function = (igame.find("x_config")).text
            y_function = (igame.find("y_config")).text
            l_function = (igame.find("l_config")).text
            r_function = (igame.find("r_config")).text
            button_functions = [a_function,
                                x_function,
                                l_function,
                                b_function,
                                y_function,
                                r_function]
            mbt.make_button_image(gamename,button_functions)

            #open the text file to make the custorm text
            pxml.createCustomMarquee(gamename,system_name)
    
        print(gamename)
