# @Time    : 2019/6/12 15:31
# @Author  : Leafage
# @File    : filters.py
# @Software: PyCharm
# @Describe: 滤波器
import cv2 as cv
import numpy as np
import utils


class VConvolutionFilter(object):
    """
    一般的卷积滤波器
    """
    def __init__(self, kernel):
        self._kernel = kernel

    def apply(self, src, dst):
        cv.filter2D(src, -1, self._kernel, dst)  # RGB or gray


class SharpenFilter(VConvolutionFilter):
    """
    特定的锐化滤波器,1-pixel radius
    """
    def __init__(self):
        kernel = np.array([[-1, -1, -1],
                           [-1, 9, -1],
                           [-1, -1, -1]])
        VConvolutionFilter.__init__(self, kernel)


class FindEdgesFilter(VConvolutionFilter):
    """
    边缘检测，把边缘转化为白色，非边缘转化为黑色
    """
    def __init__(self):
        kernel = np.array([[-1, -1, -1],
                           [-1, 8, -1],
                           [-1, -1, -1]])
        VConvolutionFilter.__init__(self, kernel)


class BlurFilter(VConvolutionFilter):
    """
    模糊滤波器
    """
    def __init__(self):
        kernel = np.array([[0.04, 0.04, 0.04, 0.04, 0.04],
                           [0.04, 0.04, 0.04, 0.04, 0.04],
                           [0.04, 0.04, 0.04, 0.04, 0.04],
                           [0.04, 0.04, 0.04, 0.04, 0.04],
                           [0.04, 0.04, 0.04, 0.04, 0.04]])
        VConvolutionFilter.__init__(self, kernel)


class EmbossFilter(VConvolutionFilter):
    """
    同时达到模糊和锐化的效果，产生ridge 或者 浮雕 embossed的效果
    """
    def __init__(self):
        kernel = np.array([[-2, -1, 0],
                           [-1, 1, 1],
                           [0, 1, 2]])
        VConvolutionFilter.__init__(self, kernel)


def strokeEdges(src, dst, blurKsize = 7, edgeKsize = 5):
    """
    边缘检测
    :param src: 待检测的原图像
    :param dst:
    :param blurKsize: 模糊函数的ksize参数,小与3 则不使用模糊处理
    :param edgeKsize: 边缘检测的ksize参数
    :return:
    """
    if blurKsize >= 3:
        blurredSrc = cv.medianBlur(src, blurKsize)  # 进行模糊
        graySrc = cv.cvtColor(blurredSrc, cv.COLOR_BGR2GRAY)  # 转为灰度图
    else:
        graySrc = cv.cvtColor(src, cv.COLOR_BGR2GRAY)

    cv.Laplacian(graySrc, cv.CV_8U, graySrc, ksize=edgeKsize)  # 进行边缘检测
    normalizedInverseAlpha = (1.0 / 255) * (255 - graySrc)  # 进行归一化
    channels = cv.split(src)  # 分离出三通道的颜色
    for channel in channels:  # 然后乘以原图像 把边缘变黑
        channel[:] = channel * normalizedInverseAlpha
    cv.merge(channels, dst)

