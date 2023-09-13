# 调用本地摄像头或者外接摄像头
# 2023.04.19 created by 徐梦昊
# https://blog.csdn.net/qq_35896136/article/details/106789377


# coding:utf-8
import cv2

# 参数为0时调用本地摄像头；参数为1时调用外接摄像头
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)

flag = cap.isOpened()
index = 1
while (flag):
    ret, frame = cap.read()
    cv2.imshow("Capture_Paizhao", frame)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('s'):  # 按下s键，进入下面的保存图片操作
        cv2.imwrite("E:/PyCharm Workspaces/" + str(index) + ".jpg", frame)
        print("save" + str(index) + ".jpg successfuly!")
        print("-------------------------")
        index += 1
    elif k == ord('q'):  # 按下q键，程序退出
        break
cap.release() # 释放摄像头
cv2.destroyAllWindows()# 释放并销毁窗口
