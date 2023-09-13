# 截图当前窗口 并存下来

# 先引入依赖包 pip install PyQt5
import win32gui
from PyQt5.QtWidgets import QApplication
import sys
 
hwnd_title = dict()
 
 
def get_all_hwnd(hwnd, mouse):
    if win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
        hwnd_title.update({hwnd: win32gui.GetWindowText(hwnd)})

 
win32gui.EnumWindows(get_all_hwnd, 0)
# print(hwnd_title.items()) 打印的是hwnd值和对应的Title
for h, t in hwnd_title.items():
    if t != "":
        print(h, t)
 
# 程序会打印窗口的hwnd[检索窗口句柄]和title，有了title就可以进行截图了。 exe文件spy++获取class和Title 其实上面打印对应的hwnd了 这个可以省略
hwnd = win32gui.FindWindow(None, 'C:\Windows\system32\cmd.exe')
print(hwnd)
app = QApplication(sys.argv)
screen = QApplication.primaryScreen()
img = screen.grabWindow(hwnd).toImage()
img.save("screenshot.jpg")