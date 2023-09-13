# 融合抓图 识别 输出识别信息三个部分
# 2023.04.15 created by 徐梦昊
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


# 抓取指定的窗口 截屏保存
def screenshot_f():
    # hwnd_title = dict()

    # def get_all_hwnd(hwnd, mouse):
    #     if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
    #         hwnd_title.update({hwnd: win32gui.GetWindowText(hwnd)})

    
    # win32gui.EnumWindows(get_all_hwnd, 0)
    # # print(hwnd_title.items()) 打印的是hwnd值和对应的Title
    # for h, t in hwnd_title.items():
    #     if t != "":
    #         print(h, t)
    

    hwnd = 133042 #  上面获取后自己填入对应窗口的hwnd 第一列
    print(hwnd)

    win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)  # 强行显示界面后才好截图
    win32gui.SetForegroundWindow(hwnd)  # 将窗口提到最前
    #  裁剪得到全图
    game_rect = win32gui.GetWindowRect(hwnd)
    src_image = ImageGrab.grab(game_rect)
    # src_image.show() #截图完用系统默认图片查看器打开 可以不打开
    src_image.save("screenshot.jpg")


# yolo 的cmd调用 生成覆盖的txt文本文件
def getcmd_f():
	'''
	处理图片
	:param url:图片地址
	:return: 图片中的人数
	'''
	cmd = r'd: && python D:\Desktop\yolov5-7.0\detect.py --weights yolov5s.pt --conf-thres 0.6 --source D:\Desktop\IOT_SoftWare\screenshot.jpg --save-txt --class 0 1 2 3 5 9 13 16  --exist-ok'
	text = os.popen(cmd).readlines()
	print(text)


def txt_spilt_f():
    f=open("D:/Desktop/yolov5-7.0/runs/detect/exp/labels/screenshot.txt","r", encoding = 'utf-8',errors='ignore')
    txt = [0,0,0,0,0,0,0,0]
    for line in f:
        # print(line.split(' ')[0]) # 一步到位
        # a = line.split(' ')[0] # a为以空格分隔之后的首个元素  仍为字符类型
        a = int(line.split(' ')[0]) # a为以空格分隔之后的首个元素 
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
    message1 = "前方共有"+ message
    print (message1)

	

if __name__ == '__main__':
    screenshot_f()
    getcmd_f()
    txt_spilt_f()