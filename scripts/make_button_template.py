import cv2
import numpy as np
import random

def make_button_image(game_zip_name,buttons):
    # Image dimensions for 16:9 aspect ratio
    width, height = 1920, 1080
    image = np.zeros((height, width, 3), dtype=np.uint8)  # Black background

    # Grid layout configuration
    rows = 2
    cols = 3
    circle_radius = 125
    text_offset_y = 50  # Vertical offset below each circle for text
    font = cv2.FONT_HERSHEY_SIMPLEX
    font_scale = 1.0
    font_color = (255, 255, 255)  # White text
    thickness_text = 2

    # Compute positions for the 2x3 grid
    x_step = width // (cols + 1)
    y_step = height // (rows + 1)

    idx = 0
    for r in range(rows):
        for c in range(cols):
            # Compute center point for each circle
            center_x = (c + 1) * x_step
            center_y = (r + 1) * y_step - text_offset_y

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
            
    # Save or display the image
    gamename = game_zip_name.replace(".zip","")
    cv2.imwrite("../instruction/" + gamename + "_buttons.png", image)
    

