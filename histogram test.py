import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('Resources/color.png', 0)
# imgRGB = cv2.imread('Resources/colorRGB.png')
# 圖像是 200*150像素
img_hist = plt.hist(img.ravel(), 256, [0, 256])
# img_hist = plt.hist(imgRGB.ravel(), 256, [0, 256])
# 垂直是像素量
# 水平是顏色
# 0是黑色
# 255 是白色
# 總共有256種灰度

cv2.imshow("Origin", img)
# cv2.imshow("RGB", imgRGB)
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()