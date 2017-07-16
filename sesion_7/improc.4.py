import cv2

im = cv2.imread("balls.jpg", 1)

(h, w, c) = im.shape

x1 = int(0.20 * w)
y1 = int(0.77 * h)

x2 = int(0.65 * w)
y2 = int(0.33 * h)

cv2.circle(im, (x1, y1), 100, (255, 255, 0), 16)

cv2.rectangle(im, (20, 20), (610, 310), (0, 0, 0), -1)
font = cv2.FONT_HERSHEY_PLAIN
cv2.putText(im,'Hola OpenCV',(100, 100), font, 4,(255,255,255), 10)
cv2.putText(im,'X: %d Y: %d' % (x1, y1),(100, 200), font, 4,(255,255,255), 10)

cv2.imwrite("save.jpg", im)