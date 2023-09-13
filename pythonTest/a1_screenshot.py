# 截图指定hwnd的窗口 并截图保存
# 先引入依赖包 pip install PyQt5
# 最开始运行的时候先注释掉下面的hwnd 以下的程序 因为hwnd我要先跑上面的程序获取 可以先放开下一行hwnd万金油运行一遍 这样不用注释
import win32gui
import win32con
from PyQt5.QtWidgets import QApplication
from PIL import ImageGrab

hwnd_title = dict()
 
 
def get_all_hwnd(hwnd, mouse):
    if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
        hwnd_title.update({hwnd: win32gui.GetWindowText(hwnd)})

 
win32gui.EnumWindows(get_all_hwnd, 0)
# print(hwnd_title.items()) 打印的是hwnd值和对应的Title
for h, t in hwnd_title.items():
    if t != "":
        print(h, t)
 
# 程序会打印窗口的hwnd[检索窗口句柄]和title，有了hwnd填入下面的变量就可以进行截图了
# hwnd = win32gui.FindWindow(None, 'C:\Windows\system32\cmd.exe')
hwnd = 658480 #  上面获取后自己填入对应窗口的hwnd 第一列
print(hwnd)

win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)  # 强行显示界面后才好截图
win32gui.SetForegroundWindow(hwnd)  # 将窗口提到最前
#  裁剪得到全图
game_rect = win32gui.GetWindowRect(hwnd)
src_image = ImageGrab.grab(game_rect)
# src_image.show() #截图完用系统默认图片查看器打开 可以不打开
src_image.save("screenshot.jpg")







#另外一个 需要新pip库 没试
# #!/usr/bin/env python
# # coding: utf-8
# import os, time
# from loginfo.log_print import get_log
# from selenium import webdriver
 
 
# def screenshot(driver):
#     # 设置截图文件保存的路径
#     path = 'F:\\Test\\loginfo'
#     path = os.path.join(path, 'ScreenShot')
#     if not os.path.exists(path):
#         os.mkdir(path)
#     # 设置要截图的文件名
#     file_name = time.strftime('%Y_%m_%d_%H_%M_%S', time.localtime()) + '.png'
#     path = os.path.join(path, file_name)
#     log = get_log('screenshot')
#     try:
#         driver.get_screenshot_as_file(path)
#         log.info('截图成功')
#     except OSError:
#         log.info('截图失败')
 
 
# if __name__ == '__main__':
#     driver0 = webdriver.Chrome()
#     screenshot(driver0)
#     driver0.quit()