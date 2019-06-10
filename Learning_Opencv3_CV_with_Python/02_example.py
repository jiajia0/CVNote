# @Time    : 2019/6/10 15:41
# @Author  : Leafage
# @File    : 02_example.py
# @Software: PyCharm
# @Describe: 第二章中的example
import cv2
import numpy as np
import os

'''
randomByteArray = bytearray(os.urandom(120000))
flatNumpyArray = np.array(randomByteArray)

grayImage = flatNumpyArray.reshape(300, 400)
cv2.imwrite('RandomGray.png', grayImage)

bgrImage = flatNumpyArray.reshape(100, 400, 3)
cv2.imwrite('RandomColor.png', bgrImage)

img = cv2.imread('RandomColor.png')

'''

'''
# 读取摄像头视频
cameraCaptuer = cv2.VideoCapture(0)
fps = 30
size = (int(cameraCaptuer.get(cv2.CAP_PROP_FRAME_WIDTH)),
        int(cameraCaptuer.get(cv2.CAP_PROP_FRAME_HEIGHT)))

videoWriter = cv2.VideoWriter(
    'yOutputVid.avi', cv2.VideoWriter_fourcc('I', '4', '2', '0'),
    fps, size)

success, frame = cameraCaptuer.read()
numFramesRemaining = 10 * fps - 1

while success and numFramesRemaining > 0:
    videoWriter.write(frame)
    success, frame = cameraCaptuer.read()
    numFramesRemaining -= 1

cameraCaptuer.release()
'''

clicked = False


def onMouse(event, x, y, flags, param):
    global clicked
    if event == cv2.EVENT_LBUTTONUP:
        clicked = True


cameraCapture = cv2.VideoCapture(0)  # 读取摄像头
# 创建窗口
cv2.namedWindow('MyWindow')
cv2.setMouseCallback('MyWindow', onMouse)

print('Showing camera feed. Click window or press any key to stop.')
# 读取frame
success, frame = cameraCapture.read()
# 等待按下按钮，并且点击
while success and cv2.waitKey(1) == -1 and not clicked:
    cv2.imshow('MyWindow', frame)
    success, frame = cameraCapture.read()

cv2.destroyWindow('MyWindow')
cameraCapture.release()
