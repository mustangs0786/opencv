import cv2 as cv

def abc(iur, show=True, name_of_window = "default"):
	if iur:
		img = cv.imread(iur)
	if show:
		cv.imshow(name_of_window,img)
		cv.waitKey(0)
		cv.destroyAllWindows()
	return img


