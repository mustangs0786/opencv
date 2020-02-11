import cv2 as cv

cap = cv.VideoCapture(0)

fourcc = cv.VideoWriter_fourcc(*'XVID')
out	  = cv.VideoWriter('output.avi',fourcc, 20.0, (640, 480))

while cap.isOpened():
	ret, frame = cap.read()
	if not ret:
		print("not receiving frame")
		break
	out.write(frame)
	cv.imshow('frame', frame)
	if cv.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
out.release()
cv.destroyAllWindows()