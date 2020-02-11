import cv2 as cv

img = cv.imread("book.jpg")
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
th = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY,11,2)
cv.imshow('original', img)
cv.imshow('new', th)
cv.waitKey(0)
cv.destroyAllWindows()
