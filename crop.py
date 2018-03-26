import numpy as np
from PIL import Image

img = Image.open("image.jpg")

img2 = img.crop((1514,982,2002,1268))

img2.save("image_crop.jpg")

