import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([110,50,50]) # H - 155
    upper_blue = np.array([130,255,255]) # H - 184

    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)

    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k = cv2.waitKey(5) & 0xFF
    if k != 255:
    	print k
    if k == 109:
	    print "Mascara guardada"
	    cv2.imwrite("mascara.jpg", mask)
	    cv2.imwrite("frame_mascara.jpg", res)
	    cv2.imwrite("frame.jpg", frame)
    if k == 27:
        break

cv2.destroyAllWindows()