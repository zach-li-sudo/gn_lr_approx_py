import cv2
import numpy as np

img = cv2.imread('spd.jpg', cv2.IMREAD_GRAYSCALE)
print('Image Dimensions: ', img.shape)

# cv2.imshow('Example-show img in window', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
