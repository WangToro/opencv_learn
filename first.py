import cv2

gray_img = cv2.imread('Resources/cat.png', -1)

cv2.imshow("img", gray_img)

cv2.waitKey(0)
