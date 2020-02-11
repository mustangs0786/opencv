import cv2
img = cv2.imread( 'im.JPG', 0)
print (img)
cv2.imshow('image',img)
k = cv2.waitKey(0)
if k == 27:
	cv2.destroyAllWindows()

elif k == ord('s'):
	cv2.imwrite('i.JPG', img)
	cv2.destroyAllWindows()