# @Time    : 2019/6/17 14:22
# @Author  : Leafage
# @File    : face_detection.py
# @Software: PyCharm
# @Describe: 人脸检测
import cv2 as cv


def detect():
    face_cascade = cv.CascadeClassifier('./cascades/haarcascade_frontalface_default.xml')
    eye_cascade = cv.CascadeClassifier('./cascades/haarcascade_eye.xml')
    camera = cv.VideoCapture(0)

    while(True):
        ret, frame = camera.read()
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)

        for (x, y, w, h) in faces:
            img = cv.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
            roi_gray = gray[y: y+h, x: x+w]
            eyes = eye_cascade.detectMultiScale(roi_gray, 1.03, 5, 0, (40, 40))
            for(ex, ey, ew, eh) in eyes:
                # 书中以下代码错误，正确的绘制坐标和长宽需要加上x 和 y
                cv.rectangle(img, (x+ex, y+ey), (x+ex+ew, y+ey+eh), (0, 255, 0), 2)
        cv.imshow('camera', frame)
        if cv.waitKey(int(1000/12)) & 0xff == ord("q"):
            break
    camera.release()
    cv.destroyAllWindows()


if __name__=="__main__":
    detect()
