# 调用ESP32-CAM的RTSP视频流 保存当前帧到指定文件位置 -- 用来优化抓取窗口 但是这样比较慢 
# 2023.04.19 created by 徐梦昊

# https://blog.csdn.net/qq_35896136/article/details/106789377

# coding:utf-8
import cv2
# url = 'rtsp://192.168.177.253:8554/mjpeg/2'
url = 'rtsp://192.168.177.253//1'

cap = cv2.VideoCapture(url)
flag = cap.isOpened()
print(flag)

# fps = cap.get(cv2.CAP_PROP_FPS)
# width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
# print(fps,width,height)

(flag,frame) = cap.read()   #读取每一帧，flag表示是否读取成功，frame为图片内容。
fileName = "D:\Desktop\IOT_SoftWare\screenshot1.jpg"
# print(fileName)
if flag == True:
    cv2.imwrite(fileName,frame,[cv2.IMWRITE_JPEG_QUALITY,100])

cap.release() # 释放摄像头
cv2.destroyAllWindows()# 释放并销毁窗口




