import cv2
import numpy as np

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


img = cv2.imread('image_crop.jpg', 1)  #reading the img in
 
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  #transfering the img from bgr to hsv

lower_orange = np.array([6,88,139], dtype=np.uint8)    #color ranges (in hsv) for orange
upper_orange = np.array([9,112,152], dtype=np.uint8)   

lower_blue = np.array([84,178,74], dtype=np.uint8)     #color ranges (in hsv) for blue 
upper_blue = np.array([87,205,86],  dtype=np.uint8)

lower_green = np.array([78,159,49], dtype=np.uint8)   #color ranges (in hsv) for green
upper_green = np.array([92,255,93], dtype=np.uint8)

lower_black = np.array([55,6,88], dtype=np.uint8)     #color ranges (in hsv) for black
upper_black = np.array([165, 31, 92], dtype=np.uint8)

lower_yellow = np.array([24,199,93], dtype=np.uint8)    #color ranges (in hsv) for yellow
upper_yellow = np.array([28,255,186], dtype=np.uint8)

#Detecting the color, and if detected seting thier value to true      
for i in range(5):

    if(i == 0):
        
        mask = cv2.inRange(hsv, lower_orange,  upper_orange)
        x1 = cv2.countNonZero(mask);
        if(x1 > x):             
            orange = True

    elif(i == 1):
         
        mask = cv2.inRange(hsv, lower_blue, upper_blue)
        x1 = cv2.countNonZero(mask)
        if(x1 > x):
            blue = True
    
    elif(i == 2):

        mask = cv2.inRange(hsv, lower_green, upper_green)
        x1 = cv2.countNonZero(mask);             
        if(x1>x):
            green = True
    
    elif(i == 3):    
       
        mask = cv2.inRange(hsv, lower_black, upper_black)
        x1 = cv2.countNonZero(mask);                              
        if(x1>x):
            black = True
             

    elif(i == 4):        
           
        mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
        x1 = cv2.countNonZero(mask);                      
        if(x1>x):
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






