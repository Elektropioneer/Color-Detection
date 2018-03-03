import cv2
import numpy as np

i = 0
x = 0

#getting the img 
img = cv2.imread('circles.png', 1)
#converting bgr to hsv
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# defineing the colors/ranges
lower_red = np.array([30,150,50], dtype=np.uint8)
upper_red = np.array([255,255,180], dtype=np.uint8)

lower_blue = np.array([108,100,100], dtype=np.uint8)
upper_blue = np.array([128,255,255],  dtype=np.uint8)

lower_green = np.array([59,100,100], dtype=np.uint8)
upper_green = np.array([79, 255, 255], dtype=np.uint8)
#going through each color ~ makeing a mask of that color and then seeing if its < than 0 
#this is not convinient because these conditions are not suitable for real life 
for i in range(3):

    if(i == 0):
        print i
        mask = cv2.inRange(hsv, lower_red,  upper_red)
        x1 = cv2.countNonZero(mask);
        if(x1 > x):
             print("red detected")
        else:
             print("red not-detected")
    elif(i == 1):
         print i
         mask = cv2.inRange(hsv, lower_blue, upper_blue)
         x1 = cv2.countNonZero(mask);
         if(x1 > x):
              print("blue detected")
         else:
              print("blue not-detected")
    elif(i == 2):
         print i
         mask = cv2.inRange(hsv, lower_green, upper_green)
         x1 = cv2.countNonZero(mask);             
         if(x1>x):
              print("green detected")
         else:
              print("green not-detected")

