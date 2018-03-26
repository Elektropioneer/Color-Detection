# A scrpit for determening the hsv for a color on a image (to use take a img you have croped (image_crop) of a single color)
import cv2 
import numpy as np
from PIL import Image

h_a = []         # setting up arrays for all hue, saturation and value values
s_a = []
v_a = []

img1 = cv2.imread('image_crop.jpg', 1) #getting the croped image

hsv = cv2.cvtColor(img1, cv2.COLOR_BGR2HSV) #transfering that img from bgr to hsv

h, s, v = cv2.split(hsv) #spliting the h,s and v channels

h_a = +h    #setting all the values of h into the array
s_a = +s    #setting all the values of s into the array
v_a = +v    #setting all the values of v into the array

print "Maximum value:" #printing the maxin values .....
print "h:" 
print np.amax(h_a)     #getting the max value of h
print "s:" 
print np.amax(s_a)     #getting the max value of s
print "v:" 
print np.amax(v_a)     #getting the max value of v

print "Minimum value:" #printing the min values ......
print "h:" 
print np.amin(h_a)     #getting the min value of h
print "s:"  
print np.amin(s_a)     #getting the min value of s
print "v:" 
print np.amin(v_a)     #getting the min value of v