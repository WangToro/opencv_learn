import cv2
from matplotlib import pyplot as plt

imgRGB = cv2.imread('Resources/houseRGB.jpg')
# 圖像是 200*150像素
color = ('b', 'g', 'r')
for i, col in enumerate(color):
    img_hist = cv2.calcHist([imgRGB], [i], None, [256], [0, 256])
    plt.plot(img_hist, color=col)
    plt.xlim([0, 256])

cv2.imshow("RGB", imgRGB)
plt.show()
cv2.waitKey(0)
cv2.destroyAllWindows()
