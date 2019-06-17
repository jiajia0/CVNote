# @Time    : 2019/6/16 19:53
# @Author  : Leafage
# @File    : cameo.py
# @Software: PyCharm
# @Describe:
import cv2 as cv
import filters
from managers import WindowManager, CaptureManager


class Cameo(object):
    def __init__(self):
        self._windowManager = WindowManager('Cameo', self.onKeypress)
        self._captureManager = CaptureManager(cv.VideoCapture(0), self._windowManager, True)
        self._curveFilter = filters.SharpenFilter()

    def run(self):
        """
        主函数循环
        :return:
        """
        self._windowManager.createWindow()
        while self._windowManager.isWindowCreated:
            self._captureManager.enterFrame()
            frame = self._captureManager.frame
            filters.strokeEdges(frame, frame)
            self._curveFilter.apply(frame, frame)
            self._captureManager.exitFrame()
            self._windowManager.processEvents()

    def onKeypress(self, keycode):
        """
        处理keypress
        space - > Take a screenshot
        tab   - > Start/stop recording a screencast
        escape - > Quit
        :param keycode:
        :return:
        """
        if keycode == 32:
            self._captureManager.writeImage('screenshot.png')
        elif keycode == 9:
            if not self._captureManager.isWritingVideo:
                self._captureManager.startWritingVideo('screencast.avi')
            else:
                self._captureManager.stopWritingVideo()
        elif keycode == 27:
            self._windowManager.destroyWindow()


if __name__=="__main__":
    Cameo().run()
