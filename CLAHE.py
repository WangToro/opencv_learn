import cv2
img = cv2.imread('Resources/lena.png',0)
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
# cliplimit 對比度大小
# tileGridSize 切割的矩形圖像大小
img_clahe = clahe.apply(img)
cv2.imshow('Origin', img)
cv2.imshow('CLAHE', img_clahe)
cv2.waitKey(0)
