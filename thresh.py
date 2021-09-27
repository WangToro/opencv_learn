import cv2
import matplotlib.pyplot as plt

img = cv2.imread("Resources/lena.png", 0)

TF, thresh1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
# 大於門檻的變成255 ,其他為0
TF, thresh2 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY_INV)
# 大於門檻的變成0 ,其他為255
TF, thresh3 = cv2.threshold(img, 127, 255, cv2.THRESH_TRUNC)
# 大於門檻的變成門檻值,其他不變
TF, thresh4 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO)
# 小於門檻值得為0,其他不變
TF, thresh5 = cv2.threshold(img, 127, 255, cv2.THRESH_TOZERO_INV)
# 大於門檻值得為0,其他不變

# TF代表True或False 因為threshold會回傳兩個值分別是 1.True或False,代表有沒有讀到圖片 2.目標圖片
# error : mat is not a numerical tuple
# 出現這個問題的原因是 cv2.threshold()返回2個參數，我開始想當然的認爲只返回一個，於是最開始直接用cv2.imshow(“BINARY”,thresh1)的時候就報錯了。添加一個佔位返回參數即可。

titles = ['Origin', 'BINARY', 'BINARY_INV', 'TRUNC', 'TOZERO', 'TOZERO_INV']
# 定義圖片名稱,存成陣列titles
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5]
# 對印圖片,按順序排列,存成新陣列images

for i in range(6):
    plt.subplot(2, 3, i+1), plt.imshow(images[i], 'gray')
    # plt.subplot(總行,總列,位置[1,2,3],[4,5,6])
    # plt.imshow(圖片變數,類型)
    plt.title(titles[i])
    # plt.imshow(圖片標題)
    plt.xticks([]), plt.yticks([])
    # plt.xticks([]) 圖片位置x軸
    # plt.yticks([]) 圖片位置y軸

plt.show()

'''
cv2.imshow('Origin', img)
cv2.imshow('BINARY', thresh1)
cv2.imshow('BINARY_INV', thresh2)
cv2.imshow('TRUNC', thresh3)
cv2.imshow('TOZERO', thresh4)
cv2.imshow('TOZERO_INV', thresh5)
'''


cv2.waitKey(0)
