# tag 更改
# 融合图像识别并发布 抓取RTSP流窗口 抓取图像保存
# 2023.04.16 created by 徐梦昊
# python3.6
# -*- coding: utf-8 -*-
import paho.mqtt.client as mqtt
import random

# -*- coding: UTF-8 -*-
# cmd依赖
import os, sys, re

# 截图指定hwnd的窗口 并截图保存
# 先引入依赖包 pip install PyQt5
# 最开始运行的时候先注释掉下面的hwnd 以下的程序 因为hwnd我要先跑上面的程序获取 可以先放开下一行hwnd万金油运行一遍 这样不用注释
# 截图依赖
import win32gui
import win32con
from PyQt5.QtWidgets import QApplication
from PIL import ImageGrab

# import win32com
import win32com.client
import pythoncom

# opencv 抓取rtsp视频流
import cv2

# 文件移动
import shutil


broker = 'broker.emqx.io'
port = 1883
topic_button = "cc36e70148924ef2bb2e1d477c24675f_button" # 订阅这个主题 等待按键发布“1”
topic_mp3 = "cc36e70148924ef2bb2e1d477c24675f_mp3" # 将识别信息发布到这个主题
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 100)}'


# 订阅函数
class MqttRoad(object):
 
    def __init__(self, mqtt_host, mqtt_port, mqtt_keepalive):
        super(MqttRoad, self).__init__()
        client = mqtt.Client()
        client.on_connect = self.on_connect
        client.on_message = self.on_message
        client.on_publish = self.on_publish
        client.connect(mqtt_host, mqtt_port, mqtt_keepalive)  # 600为keepalive的时间间隔
        client.loop_forever()  # 保持连接
 
    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code: " + str(rc))
        # 订阅 #tag
        client.subscribe(topic_button)
 
 
    def on_message(self, client, userdata, msg):
        print("on_message topic:" + msg.topic + " message:" + str(msg.payload.decode('utf-8')))
        strmqtt = str(msg.payload.decode('utf-8'))
        #tag 接收消息 进行判断
        if strmqtt == "1":
            print("接收到按键请求，请求发布画面识别的语音播报,下面开始依次抓取、执行识别命令、处理文本、发布消息！")
            # 可以先注释下面的摄像头抓取图像的函数  把希望检测测试的图像保存在本项目的根目录下 命名为screenshot.jpg 就可以进行其他流程的测试 结果的输出的测试
            screenshot_f()
            print("抓取成功！下面执行yolo算法---")

            getcmd_f()
            print("执行识别命令已经成功完成！")

            # 识别的图像文件到达YoloImages文件夹下
            file_f()
            print("图像识别画面文件移动已经成功完成！")

            # 识别的txt文件处理 并把重新组织好的文字保存为yolo.txt 到达YoloImages文件夹下
            txt_spilt_f()
            print("处理文本成功完成！")

            publish()
            print("识别信息已发布成功！")
            print(" ######################################### ")
        else:
            print("接收到按键请求，请求发布画面识别的语音播报,下面开始依次抓取、执行识别命令、处理文本、发布消息！")
            screenshot_f()
            print("抓取成功！下面执行yolo算法---")

            getcmd_f()
            print("执行识别命令已经成功完成！")

            file_f()
            print("图像识别画面文件移动已经成功完成！")

            txt_spilt_f()
            print("处理文本成功完成！")
            print(" ######################################### ")
        
 
    #   订阅回调
    def on_subscribe(self, client, userdata, mid, granted_qos):
        print("On Subscribed: qos = %d" % granted_qos)
        pass
 
    #   取消订阅回调
    def on_unsubscribe(self, client, userdata, mid):
        # print("取消订阅")
        print("On unSubscribed: qos = %d" % mid)
        pass
 
    #   发布消息回调
    def on_publish(self, client, userdata, mid):
        # print("发布消息")
        print("On onPublish: qos = %d" % mid)
        pass
 
    #   断开链接回调
    def on_disconnect(self, client, userdata, rc):
        # print("断开链接")
        print("Unexpected disconnection rc = " + str(rc))
        pass
 
# 发布函数
def publish():
    def on_connect(client, userdata, flags, rc):
        print ("链接")
        print("Connected with result code: " + str(rc))
    
    
    def on_message(client, userdata, msg):
        print ("消息内容")
        print(msg.topic + " " + str(msg.payload))
    
    
    #   订阅回调
    def on_subscribe(client, userdata, mid, granted_qos):
        print ("订阅")
        print("On Subscribed: qos = %d" % granted_qos)
        pass
    
    
    #   取消订阅回调
    def on_unsubscribe(client, userdata, mid, granted_qos):
        print ("取消订阅")
        print("On unSubscribed: qos = %d" % granted_qos)
        pass
    
    
    #   发布消息回调
    def on_publish(client, userdata, mid):
        print ("发布消息")
        print("On onPublish: qos = %d" % mid)
        pass
    
    
    #   断开链接回调
    def on_disconnect(client, userdata, rc):
        print ("断开链接")
        print("Unexpected disconnection rc = " + str(rc))
        pass
    
    
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.on_publish = on_publish
    client.on_disconnect = on_disconnect
    client.on_unsubscribe = on_unsubscribe
    client.on_subscribe = on_subscribe
    client.connect(broker, 1883, 600) # 600为keepalive的时间间隔

    # client.publish(topic_mp3, payload='前方共有1个人 3辆汽车 1条狗 ', qos=0, retain=False) #tag发布消息
    client.publish(topic_mp3, payload = message2, qos=0, retain=False) #message1为完整信息 message2为8位代码
    


# 抓取RTSP流窗口 抓取图像保存
def screenshot_f():
    # 更改
    url = 'rtsp://192.168.95.253:8554/mjpeg/2'
    cap = cv2.VideoCapture(url)
    flag = cap.isOpened()
    print(flag)

    # fps = cap.get(cv2.CAP_PROP_FPS)
    # width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    # height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    # print(fps,width,height)

    (flag,frame) = cap.read()   #读取每一帧，flag表示是否读取成功，frame为图片内容。
    fileName = "D:\Desktop\IOT_SoftWare\screenshot.jpg"
    # print(fileName)
    if flag == True:
        cv2.imwrite(fileName,frame,[cv2.IMWRITE_JPEG_QUALITY,100])

    cap.release() # 释放摄像头
    cv2.destroyAllWindows()# 释放并销毁窗口


# yolo 的cmd调用 生成覆盖的txt文本文件
def getcmd_f():
	'''
	处理图片
	:param url:图片地址
	:return: 图片中的人数
	'''
	cmd = r'd: && python D:\Desktop\yolov5-7.0\detect.py --weights yolov5s.pt --conf-thres 0.6 --source D:\Desktop\IOT_SoftWare\screenshot.jpg --save-txt --class 0 1 2 3 5 9 13 16  --exist-ok'
	text = os.popen(cmd).readlines()
	print(text) #读不出来 只好读txt文件了



# txt文本信息处理
def txt_spilt_f():
    f=open("D:/Desktop/yolov5-7.0/runs/detect/exp/labels/screenshot.txt","r", encoding = 'utf-8',errors='ignore')
    txt = [0,0,0,0,0,0,0,0]
    for line in f:
        # print(line.split(' ')[0]) # 一步到位
        # a = line.split(' ')[0] # a为以空格分隔之后的首个元素  仍为字符类型
        a = int(line.split(' ')[0]) # a为以空格分隔之后的首个元素[0]  每一行一共五列 [0]-[4] 
        # print(a)
        if a == 0:# 人
            txt[0] = txt[0] +1
        if a == 1: # 自行车
            txt[1] = txt[1] +1
        if a == 2: # 汽车
            txt[2] = txt[2] +1
        if a == 3: # 摩托车
            txt[3] = txt[3] +1
        if a == 5: # 公共汽车
            txt[4] = txt[4] +1
        if a == 9: # 交通灯
            txt[5] = txt[5] +1
        if a == 13: # 长椅
            txt[6] = txt[6] +1
        if a == 16: # 狗
            txt[7] = txt[7] +1

    message = ""
    if txt[0] != 0:# 人
        message = str(txt[0]) +"个人 "
    if txt[1] != 0: # 自行车
        message = message +  str(txt[1]) +"辆自行车 "
    if txt[2] != 0: # 汽车
        message = message +  str(txt[2]) +"辆汽车 "
    if txt[3] != 0: # 摩托车
        message = message +  str(txt[3]) +"辆摩托车 "
    if txt[4] != 0: # 公共汽车
        message = message +  str(txt[4]) +"辆公共汽车 "
    if txt[5] != 0: # 交通灯
        message = message +  str(txt[5]) +"个交通灯 "
    if txt[6] != 0: # 长椅
        message = message +  str(txt[6]) +"个长椅 "
    if txt[7] != 0: # 狗
        message = message +  str(txt[7]) +"条狗 "
    global message1 # 识别的完整结果
    global message2 # 识别结果以8个十进制数展示 ，每个种类的数目不能大于9
    message2 = str(txt[0])+str(txt[1])+str(txt[2])+str(txt[3])+str(txt[4])+str(txt[5])+str(txt[6])+str(txt[7])
    if message2 == '00000000':
        message1 = "前方未检测到事物"
    else:
        message1= "前方共有"+ message
    print("message1:",end="");print (message1)
    # 识别的完整信息书写到txt文件当中
    with open('D:\\Desktop\\IOT_SoftWare\\app01\\static\\YoloImages\\yolo.txt', 'w', encoding='utf-8') as f:
        f.write(message1)

    print("message2:",end="");print (message2)

# 移动识别过后的图片位置
def file_f():
        argetdir_path = 'D:\\Desktop\\yolov5-7.0\\runs\\detect\\exp\\screenshot.jpg'
        Targetfile_path = 'D:\\Desktop\\IOT_SoftWare\\app01\\static\\YoloImages\\screenshot_django.jpg'
        shutil.copyfile(argetdir_path, Targetfile_path)

 
if __name__ == '__main__':
    MqttRoad(broker, 1883, 600)



