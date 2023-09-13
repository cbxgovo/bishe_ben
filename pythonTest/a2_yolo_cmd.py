#!/usr/bin/python
# -*- coding: UTF-8 -*-

import os, sys, re

# yolo 调用
# def getperson(url:str) -> int:
def getperson():
	'''
	处理图片
	:param url:图片地址
	:return: 图片中的人数
	'''
	# cmd = r'd: && python D:\Desktop\yolov5-7.0\detect.py --weights yolov5s.pt --source ' + url 
	cmd = r'd: && python D:\Desktop\yolov5-7.0\detect.py --weights yolov5s.pt --source D:\Desktop\IOT_SoftWare\screenshot.jpg --save-txt --class 0 1 2 3 5 9 13 16  --exist-ok'
    
	# cmd默认从C盘开始执行的 项目和环境不在一起 需要先切换到D盘再执行才可以不出错 在系统窗的适合
	# cmd = r'd: && python D:\Desktop\yolov5-7.0\detect.py --weights yolov5s.pt --source ' + url 
        
	# cmd 看python的版本可以打印出来 但是我打印识别的信息就是空的   额外：窗口灰色为print打印
	# cmd = 'python --version'
	# result = os.popen(cmd,'r',2000)

	text = os.popen(cmd).readlines()
	print(text)
	str1 = str(text)
	print(str1)

	# result = os.popen(cmd)
	# print('********************0')
	# # os.system(cmd)
	# print(result) # 输出 <os._wrap_close object at 0x000002559927EF10>
	# context = result.read()
	# for line in context.splitlines():
	# 	print(line)
	# result.close()
	

if __name__ == '__main__':
    getperson()
 




########################################################


#mqtt py测试
# # -*- coding: utf-8 -*-

# from paho.mqtt import client as mqtt_client
# import time

# broker = 'broker.emqx.io'
# port = 1883
# topic = "cc36e70148924ef2bb2e1d477c24675f"
# client_id = f'43f90020d29d491c9e671db1ee5b8db7'

# def connect_mqtt() -> mqtt_client:
#     def on_connect(client, userdata, flags, rc):
#         if rc == 0:
#             print("Connected to MQTT Broker!")
#         else:
#             print("Failed to connect, return code %d\n", rc)
#     client = mqtt_client.Client(client_id)
#     client.on_connect = on_connect
#     client.connect(broker, port)
#     return client


# def subscribe(client: mqtt_client):
#     def on_message(client, userdata, msg):
#         print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
#     client.subscribe(topic)
#     client.on_message = on_message



# client = connect_mqtt()
# subscribe(client)
# client.loop_forever()



########################################################


# # 字符串分割测试
# a = "dog, cat; cat, dog"
# b1 = a.split(' ')
# b2 = a.split(',')
# b3 = a.split(';')
# print(a,'\n',b1,'\n',b2,'\n',b3)

# print(b2[0],b2[1],b2[2])

# 输出如下：
# dog, cat; cat, dog 
# ['dog,', 'cat;', 'cat,', 'dog'] 
# ['dog', ' cat; cat', ' dog']
# ['dog, cat', ' cat, dog']
