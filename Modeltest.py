import cv2
import numpy as np

img = cv2.imread("D:/Desktop/IRS/Image_Recognition_System/TestingPic/test.jpg")

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# mask of green (36,25,25) ~ (86, 255,255)
mask = cv2.inRange(hsv, (36, 25, 25), (70, 255,255))

green = cv2.bitwise_and(img,img, mask= mask)
cv2.namedWindow('Image', cv2.WINDOW_NORMAL)

cv2.imshow('Image', green)
cv2.waitKey(0)
cv2.destroyAllWindows()