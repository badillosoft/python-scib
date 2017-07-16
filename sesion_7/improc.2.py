import cv2

im = cv2.imread("balls.jpg", 0)

cv2.imwrite("balls_g.jpg", im)