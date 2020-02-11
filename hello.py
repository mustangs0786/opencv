import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('im.JPG',0)


plt.imshow(img, cmap = '', interpolation = 'bicubic')
plt.show()
