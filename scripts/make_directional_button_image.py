#!/usr/bin/python3

import make_button_template as mbt 
import sys

print(f"Script name: {sys.argv[0]}")
if len(sys.argv) > 1:
    system_name = sys.argv[1]
    print(f"Processing for system: {system_name}\n")
else:
    print("system name needs to be used")
    exit

saveImage = False

joystick = [sys.argv[1],
            sys.argv[2],
            sys.argv[3],
            sys.argv[4]
           ]

buttons = [sys.argv[5],
           sys.argv[6],
           sys.argv[7],
           sys.argv[8],
           sys.argv[9],
           sys.argv[10],
          ]

typename = sys.argv[11]
direction = sys.argv[12]

mbt.drawArrows(joystick,buttons,typename,direction)

if (saveImage):
	pxml.addDirectionalImageTypeToXML(joystick,buttons,typename,direction)

