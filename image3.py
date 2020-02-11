import cv2 as cv
img = cv.imread('im.JPG', 0)
font = cv.FONT_HERSHEY_SIMPLEX
cv.putText(img,'OpenCV',(10,500),font,4,(255,255,255),2,cv.LINE_AA)
cv.line(img,(0,0),(511,511),(255,0,0),5)
cv.namedWindow('image', cv.WINDOW_NORMAL)
cv.imshow("image",img)
cv.waitKey(0);
cv.destroyAllWindows()