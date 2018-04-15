import numpy as np
from PIL import Image

img = Image.open("image.jpg")

img2 = img.crop((1128,836,1652,1123))

img2.save("image_crop.jpg")

