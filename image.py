import cv2
import numpy as np
from heapq import nlargest

x = 5   # variable for color comparison

orange = False  # bool's for posible detected colors
blue = False
green = False
black = False
yellow = False

array1 = ['orange, black, green']   #  all
array2 = ['yellow, black, blue']    #      posible
array3 = ['blue, green, orange']    #             color
array4 = ['yellow, green, black']   #                 combinations
array5 = ['black, yellow, orange']
array6 = ['green, yellow, blue']
array7 = ['blue, orange, black']
array8 = ['green, orange, yellow']
array9 = ['black, blue, green']
array10 = ['orange, blue, yellow']

temp = []   #arrays for sorting
temp2 = []
temp3 = []
temp4 = []

img = cv2.imread('image_crop.jpg', 1)  #reading the img in

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  #transfering the img from bgr to hsv

lower_orange = np.array([14,222,132], dtype=np.uint8)    #color ranges (in hsv) for orange
upper_orange = np.array([16,255,177], dtype=np.uint8)

lower_blue = np.array([77,82,59], dtype=np.uint8)     #color ranges (in hsv) for blue
upper_blue = np.array([92,207,118],  dtype=np.uint8)

lower_green = np.array([33,205,90], dtype=np.uint8)   #color ranges (in hsv) for green
upper_green = np.array([46,255,170], dtype=np.uint8)

lower_black = np.array([16,95,24], dtype=np.uint8)     #color ranges (in hsv) for black
upper_black = np.array([33, 255, 75], dtype=np.uint8)

lower_yellow = np.array([24,199,93], dtype=np.uint8)    #color ranges (in hsv) for yellow
upper_yellow = np.array([28,255,186], dtype=np.uint8)


mask = cv2.inRange(hsv, lower_orange,  upper_orange)
x_o = cv2.countNonZero(mask)

mask = cv2.inRange(hsv, lower_blue,  upper_blue)
x_b = cv2.countNonZero(mask)

mask = cv2.inRange(hsv, lower_green, upper_green)
x_g = cv2.countNonZero(mask)

mask = cv2.inRange(hsv, lower_black, upper_black)
x_blc = cv2.countNonZero(mask)

mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
x_y = cv2.countNonZero(mask)

#Detecting the color, and if detected seting thier value to true

if(x_o > x):
    temp.append(x_o)
    print "orange"
    print x_o
if(x_b > x):
    temp.append(x_b)
    print "blue"
    print x_b
if(x_g > x):
    temp.append(x_g)
    print "green"
    print x_g
if(x_blc > x):
    temp.append(x_blc)
    print "black"
    print x_blc
if(x_y > x):
    temp.append(x_y)
    print "yellow"
    print x_y

temp2.extend(tuple(temp))

temp2.sort()

temp3 = temp2[::-1]

temp4.extend(temp3[:3])

print temp2
print temp3
print temp4

if(x_o in temp4):
    orange = True
if(x_b in temp4):
    blue = True
if(x_g in temp4):
    green = True
if(x_blc in temp4):
    black = True
if(x_y in temp4):
    yellow = True


#Printing the combination(array) detected
if(orange == True & black == True & green == True):
    print(array1)

elif(yellow == True & black == True & blue == True):
    print(array2)

elif(blue == True & green == True & orange == True):
    print(array3)

elif(yellow == True & green == True & black == True):
    print(array4)

elif(black == True & yellow == True & orange == True):
    print(array5)

elif(green == True & yellow == True & blue == True):
    print(array6)

elif(blue == True & orange == True & black == True):
    print(array7)

elif(green == True & orange == True & yellow == True):
    print(array8)

elif(black == True & blue == True & green == True):
    print(array9)

elif(orange == True & blue == True & yellow == True):
    print(array10)






