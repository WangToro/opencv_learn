import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('Resources/lena.png', 0)
# img_hist = plt.hist(img.ravel(), 256, [0, 256])
# plt.hist() 繪製直方圖
# ravel 將多維降為一維
# 通過函式ravel()拉直影像

'''
# RGB
imgRGB = cv2.imread('Resources/lena.png')
color = ('b', 'g', 'r')
for i, col in enumerate(color):
    img_histr = cv2.calcHist([imgRGB], [i], None, [256], [0,256])
    img_histrgb = plt.plot(img_histr, color=col)
    plt.xlim([0, 256])
'''
equ = cv2.equalizeHist(img)
img_equ = plt.hist(equ.ravel(), 256, [0, 255])

cv2.imshow("Origin", img)
cv2.imshow("equal_image", equ)
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
