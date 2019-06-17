# @Time    : 2019/6/12 15:02
# @Author  : Leafage
# @File    : 03_example.py
# @Software: PyCharm
# @Describe: 第三章中的例子
import cv2 as cv
import numpy as np
from scipy import ndimage



'''
# 轮廓检测
img = np.zeros((200, 200), dtype=np.uint8)
img[50: 150, 50: 150] = 255

ret, thresh = cv.threshold(img, 127, 255, 0)
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
color = cv.cvtColor(img, cv.COLOR_GRAY2BGR)

img = cv.drawContours(color, contours, -1, (0, 255, 0), 2)
cv.imshow('contours', color)
cv.waitKey()
cv.destroyAllWindows()
'''

'''
# 自定义卷积核：3x3 5x5
kernel_3x3 = np.array([[-1, -1, -1],
                       [-1, 8, -1],
                       [-1, -1, -1]])
kernel_5x5 = np.array([[-1, -1, -1, -1, -1],
                       [-1, 1, 2, 1, -1],
                       [-1, 2, 4, 2, -1],
                       [-1, 1, 2, 1, -1],
                       [-1, -1, -1, -1, -1]])

img = cv.imread(r"F:\GitRepository\CVNote\OpenCVNote\test1.jpg", 0)

k3 = ndimage.convolve(img, kernel_3x3)
k5 = ndimage.convolve(img, kernel_5x5)

# 使用低通滤波器之后，与原始图像计算差值
blurred = cv.GaussianBlur(img, (11, 11), 0)
g_hpf = img - blurred

cv.imshow('3x3', k3)
cv.imshow('5x5', k5)
cv.imshow('g_hpf', g_hpf)
cv.waitKey()
cv.destroyAllWindows()
'''