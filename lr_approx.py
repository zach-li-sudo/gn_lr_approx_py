import numpy as np

from PIL import Image

image = Image.open('./icon-py.png')
# summarize some details about the image
print(image.format)
print(image.size)
print(image.mode)
# show the image
# load_image.show()