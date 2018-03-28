#!/bin/bash

#fswebcam --no-banner  --set brightness=80% --fps 15 -S 8 -r 1080x920 image.jpg

sudo raspistill --awb sun -o image.jpg

python crop.py

python image.py

scp -r image.jpg image_crop.jpg kurdish_yoda@192.168.0.108:Projects/pi_stuff/images


sudo rm image.jpg image_crop.jpg
