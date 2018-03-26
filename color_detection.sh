#!/bin/bash

fswebcam --no-banner  --set brightness=80% --fps 15 -S 8 -r 1080x920 image.jpg

python3 crop.py

python3 image.py



scp -r image.jpg image_crop.jpg kurdish_yoda@192.168.43.147:pi_stuff/color_detection/images


rm image.jpg image_crop.jpg
