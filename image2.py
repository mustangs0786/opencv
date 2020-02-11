import cv2
img = cv2.imread('im.JPG',0)
cv2.rectangle(img,(0,0),(150,150),(255,0,255),200)
cv2.circle(img,(100,63),55,(0,255,0),1)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'opencv',(10,500),font,4,(0,255,255),10,cv2.LINE_AA)


cv2.imshow('image',img)
#print (img)
cv2.waitKey(0)
cv2.destroyAllWindows