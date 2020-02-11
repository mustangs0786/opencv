import cv2 as cv
import numpy as np

img = cv.imread('im.JPG',0)

px = img[100:150,100:150]
print (px)
pri

cv.namedWindow('image',cv.WINDOW_NORMAL)
cv.imshow('image',img)
cv.waitKey(0);
