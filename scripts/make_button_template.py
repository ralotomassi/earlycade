import cv2
import numpy as np
import random
import os

#constants that represent joystick movement
HORIZONTAL = 0
VERTICAL = 1
ALL = 2
def drawLeftArrow(canvas,xStart,yStart,width,length,arrowWidth,arrowLength,text):

    # 2. Define 7 vertices for a block arrow pointing right
    # Coordinates trace the tail, the neck corners, the arrowhead corners, and the tip
    halfWidth = int(width/2)
    halfArrow = int(arrowWidth/2)
    pointA = [xStart,yStart+halfWidth]
    pointB = [xStart-length,yStart+halfWidth]
    pointC = [xStart-length,yStart+halfArrow]
    pointD = [xStart-(length+arrowLength),yStart]
    pointE = [xStart-length,yStart - halfArrow]
    pointF = [xStart-length,yStart-halfWidth]
    pointG = [xStart,yStart-halfWidth]


    drawBlockArrow(canvas,pointA,pointB,pointC,pointD,pointE,pointF,pointG)

    # 5. Optional: Draw a dark green border outline around the arrow
    #cv2.polylines(canvas, [arrow_vertices], isClosed=True, color=(0, 180, 0), thickness=3)
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1.0
    font_color = (255, 255, 255)  # White text
    thickness_text = 2
    text_offset_y = 25
        
    # Get text size to center text
    text_size = cv2.getTextSize(text, font, font_scale, thickness_text)[0]
    text_x = xStart - ((length+arrowLength)//2) - (text_size[0] // 2)
    text_y = yStart + text_offset_y + halfArrow
    cv2.putText(canvas, text, (text_x, text_y), font, font_scale, font_color, thickness_text)
    

def drawRightArrow(canvas,xStart,yStart,width,length,arrowWidth,arrowLength,text):

    #Define 7 vertices for a block arrow pointing right
    # Coordinates trace the tail, the neck corners, the arrowhead corners, and the tip
    halfWidth = int(width/2)
    halfArrow = int(arrowWidth/2)
    pointA = [xStart,yStart+halfWidth]
    pointB = [xStart+length,yStart+halfWidth]
    pointC = [xStart+length,yStart+halfArrow]
    pointD = [xStart+length+arrowLength,yStart]
    pointE = [xStart+length,yStart - halfArrow]
    pointF = [xStart+length,yStart-halfWidth]
    pointG = [xStart,yStart-halfWidth]

    # 1. Create a black canvas (500x500 pixels, 3 color channels)
    #canvas = np.zeros((540, 960, 3), dtype=np.uint8)


    drawBlockArrow(canvas,pointA,pointB,pointC,pointD,pointE,pointF,pointG)

    # 5. Optional: Draw a dark green border outline around the arrow
    #cv2.polylines(canvas, [arrow_vertices], isClosed=True, color=(0, 180, 0), thickness=3)
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1.0
    font_color = (255, 255, 255)  # White text
    thickness_text = 2
    text_offset_y = 25
        
    # Get text size to center text
    text_size = cv2.getTextSize(text, font, font_scale, thickness_text)[0]
    text_x = xStart +((length+arrowLength)//2) - (text_size[0] // 2)
    text_y = yStart + text_offset_y + halfArrow
    cv2.putText(canvas, text, (text_x, text_y), font, font_scale, font_color, thickness_text)

def drawUpArrow(canvas,xStart,yStart,width,length,arrowWidth,arrowLength,text):

    halfWidth = int(width/2)
    halfArrow = int(arrowWidth/2)
    pointA = [xStart+halfWidth,yStart]
    pointB = [xStart+halfWidth,yStart-length]
    pointC = [xStart+halfArrow,yStart-length]
    pointD = [xStart,yStart-(length+arrowLength)]
    pointE = [xStart - halfArrow,yStart-length]
    pointF = [xStart-halfWidth,yStart-length]
    pointG = [xStart-halfWidth,yStart]

    drawBlockArrow(canvas,pointA,pointB,pointC,pointD,pointE,pointF,pointG)

    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1.0
    font_color = (255, 255, 255)  # White text
    thickness_text = 2
    text_offset_y = 25
        
    # Get text size to center text
    text_size = cv2.getTextSize(text, font, font_scale, thickness_text)[0]
    text_x = xStart - text_size[0] // 2
    text_y = yStart - (length + arrowLength + text_offset_y)
    cv2.putText(canvas, text, (text_x, text_y), font, font_scale, font_color, thickness_text)

def drawBlockArrow(canvas,pointA,pointB,pointC,pointD,pointE,pointF,pointG):

    # 2. Define 7 vertices for a block arrow pointing right
    # Coordinates trace the tail, the neck corners, the arrowhead corners, and the tip
    arrow_vertices = np.array([
    pointA,  # Top-left of tail
    pointB,  # Top-right of tail (neck)
    pointC,  # Top corner of arrowhead
    pointD,  # Tip of the arrow
    pointE,  # Bottom corner of arrowhead
    pointF,  # Bottom-right of tail (neck)
    pointG   # Bottom-left of tail
    ], dtype=np.int32)

    # 3. Reshape array to fit OpenCV's required format: (Number of Polygons, Points, 1, 2)
    arrow_vertices = arrow_vertices.reshape((-1, 1, 2))

    # 4. Draw the filled block arrow (Green color in BGR format)
    cv2.fillPoly(canvas, [arrow_vertices], color=(255, 255, 255))

    # 5. Optional: Draw a dark green border outline around the arrow
    #cv2.polylines(canvas, [arrow_vertices], isClosed=True, color=(0, 180, 0), thickness=3)
 

def drawDownArrow(canvas,xStart,yStart,width,length,arrowWidth,arrowLength,text):

    #Define 7 vertices for a block arrow pointing right
    # Coordinates trace the tail, the neck corners, the arrowhead corners, and the tip
    halfWidth = int(width/2)
    halfArrow = int(arrowWidth/2)
    pointA = [xStart+halfWidth,yStart]
    pointB = [xStart+halfWidth,yStart+length]
    pointC = [xStart+halfArrow,yStart+length]
    pointD = [xStart,yStart+(length+arrowLength)]
    pointE = [xStart - halfArrow,yStart+length]
    pointF = [xStart-halfWidth,yStart+length]
    pointG = [xStart-halfWidth,yStart]

    
    drawBlockArrow(canvas,pointA,pointB,pointC,pointD,pointE,pointF,pointG)

    # 5. Optional: Draw a dark green border outline around the arrow
    #cv2.polylines(canvas, [arrow_vertices], isClosed=True, color=(0, 180, 0), thickness=3)
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1.0
    font_color = (255, 255, 255)  # White text
    thickness_text = 2
    text_offset_y = 25

    # Get text size to center text
    text_size = cv2.getTextSize(text, font, font_scale, thickness_text)[0]
    text_x = xStart - text_size[0] // 2
    text_y = yStart + length + arrowLength + text_offset_y
    cv2.putText(canvas, text, (text_x, text_y), font, font_scale, font_color, thickness_text)

def drawArrows(joystick,buttons,gamename,direction):
    #set up the arrow dimensions these hard-coded values were found thru trial and error
    xStart = 200
    yStart = 270
    width = 20
    length = 60
    arrowWidth = 60
    arrowLength = 30

    print(f"direction is {direction} and ALL is {ALL}")

    # Create a black canvas (540x960 pixels, 3 color channels)
    canvas = np.zeros((540, 960, 3), dtype=np.uint8)

    circle_radius = 30
    arrow_buffer = circle_radius + 25
    button_color = (255,255,255)

    #Draw filled white circle
    cv2.circle(canvas, (xStart, yStart), circle_radius, button_color, thickness=-1)

    if ((int(direction) == HORIZONTAL) or (int(direction) == ALL)):
        print("Making horizontal arrows")
        drawLeftArrow(canvas,xStart-arrow_buffer,yStart,width,length,arrowWidth,arrowLength,joystick[3])
        drawRightArrow(canvas,xStart+arrow_buffer,yStart,width,length,arrowWidth,arrowLength,joystick[1])
    if ((int(direction) == VERTICAL) or (int(direction) == ALL)):
        print("Making vertical arrows")
        drawUpArrow(canvas,xStart,yStart - arrow_buffer,width,length,arrowWidth,arrowLength,joystick[0])
        drawDownArrow(canvas,xStart,yStart + arrow_buffer,width,length,arrowWidth,arrowLength,joystick[2])
        
    
    xPos = xStart+arrow_buffer+length+arrowLength
    make_buttons(canvas,buttons, xPos)

    # 6. Display the image
    #cv2.imshow("Move image", canvas)
    #cv2.waitKey(0)
    #cv2.destroyAllWindows()

    # Save or display the image
    #gamename = game_zip_name.replace(".zip","")
    cv2.imwrite(os.environ["INSTRUCTION_DIR"] + gamename + ".png", canvas)

def make_button_image(game_zip_name,buttons):
    # Image dimensions for 16:9 aspect ratio
    width, height = 1920, 1080
    image = np.zeros((height, width, 3), dtype=np.uint8)  # Black background

    # Grid layout configuration
    rows = 2
    cols = 3
    circle_radius = 175
    text_offset_y = 75  # Vertical offset below each circle for text
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 2.0
    font_color = (255, 255, 255)  # White text
    thickness_text = 5


    # Compute positions for the 2x3 grid
    x_step = width // (cols + 1)
    y_step = height // (rows + 1)

    #set the button positions
    circle_diameter = circle_radius * 2
    y_distance = 360 - ((2/3) * circle_diameter)
    y1 = y_distance + (circle_diameter/2)
    y2 = (y_distance * 2) + circle_diameter + circle_radius

    x_distance = 480 - ((3/4) * circle_diameter)
    x1 = x_distance + circle_radius
    x2 = (2 * x_distance) + circle_diameter + circle_radius
    x3 = (3 * x_distance) + (2 * circle_diameter) + circle_radius
    #x_positions = [1920/4,1920/2,1920-(1920/4)]
    #y_positions = [1080/3,1080-(1080/3)]
    x_positions = [x1,x2,x3]
    y_positions = [y1,y2]

    idx = 0
    for r in range(rows):
        for c in range(cols):
            # Compute center point for each circle
            #center_x = (c + 1) * x_step
            #center_y = (r + 1) * y_step - text_offset_y
            center_x = int(x_positions[c])
            center_y = int(y_positions[r])

            # Add team text underneath
            text = buttons[idx]
            idx += 1

            #get color based on text
            if (text == "off"):
                button_color = (122,122,122)
                text = ""
            else:
                button_color = (0,0,255)
            
            # Draw filled red circle
            cv2.circle(image, (center_x, center_y), circle_radius, button_color, thickness=-1)
            
            
            
            # Get text size to center text
            text_size = cv2.getTextSize(text, font, font_scale, thickness_text)[0]
            text_x = center_x - text_size[0] // 2
            text_y = center_y + circle_radius + text_offset_y
            
            cv2.putText(image, text, (text_x, text_y), font, font_scale, font_color, thickness_text)

            #write the button label
            text_size = cv2.getTextSize("A", font, font_scale, thickness_text)[0]
            x_text_pos = center_x - (text_size[0]//2)
            button_label = [["A","X","L"],
                           ["B","Y","R"]]
            cv2.putText(image, button_label[r][c],(x_text_pos,center_y), font, font_scale, font_color, thickness_text)
            
    # Save or display the image
    gamename = game_zip_name.replace(".zip","")
    cv2.imwrite(os.environ["INSTRUCTION_DIR"] + gamename + "_buttons.png", image)
    
def make_buttons(image,buttons,xPos):

    screen_width = 960
    screen_height = 540
    
    # Grid layout configuration
    rows = 2
    cols = 3
    circle_radius = 75
    text_offset_y = 30  # Vertical offset below each circle for text
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = .75
    font_color = (255, 255, 255)  # White text
    thickness_text = 2

    #set the button positions
    circle_diameter = circle_radius * 2
    y_distance = (screen_height/3) - ((2/3) * circle_diameter)
    y1 = y_distance + (circle_diameter/2)
    y2 = (y_distance * 2) + circle_diameter + circle_radius

    x2 = (screen_width + xPos)//2
    x1 = ((x2-circle_radius) + xPos)//2
    x3 = ((x2 +circle_radius) + screen_width)//2

    #x_positions = [1920/4,1920/2,1920-(1920/4)]
    #y_positions = [1080/3,1080-(1080/3)]
    x_positions = [x1,x2,x3]
    y_positions = [y1,y2]

    idx = 0
    for r in range(rows):
        for c in range(cols):
            # Compute center point for each circle
            #center_x = (c + 1) * x_step
            #center_y = (r + 1) * y_step - text_offset_y
            center_x = int(x_positions[c])
            center_y = int(y_positions[r])

            # Add team text underneath
            text = buttons[idx]
            idx += 1

            #get color based on text
            if (text == "off"):
                button_color = (122,122,122)
                text = ""
            else:
                button_color = (0,0,255)
            
            # Draw filled red circle
            cv2.circle(image, (center_x, center_y), circle_radius, button_color, thickness=-1)
            
            
            
            # Get text size to center text
            text_size = cv2.getTextSize(text, font, font_scale, thickness_text)[0]
            text_x = center_x - text_size[0] // 2
            text_y = center_y + circle_radius + text_offset_y
            
            cv2.putText(image, text, (text_x, text_y), font, font_scale, font_color, thickness_text)

            #write the button label
            text_size = cv2.getTextSize("A", font, font_scale, thickness_text)[0]
            x_text_pos = center_x - (text_size[0]//2)
            button_label = [["A","X","L"],
                           ["B","Y","R"]]
            cv2.putText(image, button_label[r][c],(x_text_pos,center_y), font, font_scale, font_color, thickness_text)

    # Save or display the image
    #gamename = game_zip_name.replace(".zip","")
    gamename = "testname"
    cv2.imwrite(os.environ["INSTRUCTION_DIR"] + gamename + "_buttons.png", image)
