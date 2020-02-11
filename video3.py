import cv2 as cv
cap = cv.VideoCapture('output.avi')
while cap.isOpened():
	ret, frame = cap.read()
	cv.imshow('frame', frame)
	if cv.waitKey(25) & 0xFF == ord('q'):
		break
cap.release()
cv.destroyAllWindows()
