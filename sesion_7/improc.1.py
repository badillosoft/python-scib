import cv2

im = cv2.imread("balls.jpg")

cv2.imshow("Balls", im)

cv2.waitKey(0)

cv2.destroyAllWindows()