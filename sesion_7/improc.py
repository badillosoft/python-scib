import numpy as np
import cv2

im = cv2.imread('pokeball.jpg')
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 127, 255, 0)

cv2.imwrite("tresh.jpg", thresh)

contours, h = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

cv2.drawContours(im, contours, -1, (255, 0, 255), 3)


for cnt in contours:
	M = cv2.moments(cnt)
	d = M['m00']
	if d == 0:
		d = 0.01
	cx = int(M['m10']/d)
	cy = int(M['m01']/d)
	cv2.line(im, (cx - 10, cy), (cx + 10, cy), (0, 255, 0), 1)
	cv2.line(im, (cx, cy - 10), (cx, cy + 10), (0, 255, 0), 1)

cv2.imwrite("balls_contours.jpg", im)