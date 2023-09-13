# # 会开启浏览器访问网页
# import time
# import webbrowser
 
# while True:  # 死循环
#     time.sleep(3 * 1)  # 程序等待时间，这里等待1min，参数的基本单位是秒
#     print("正在访问：请稍等。。。")
#     webbrowser.open(
#         "https://blog.csdn.net/xun527/article/details/88059666")  # 打开指定网页
    


#python3
 
import time  # 时间函数库，包含休眠函数sleep()
from urllib import request
 
# 希望刷阅读量的文章的URL
url = 'http://127.0.0.1:8000/contact/'
data = ''  # 将GET方法中待发送的数据设置为空
 
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko'}
 
count = 0  # 初始化计数器
# 组装GET方法的请求
req = request.Request(url='%s%s%s' % (url, '?', data), headers=headers)
while 1:  # 一旦开刷就停不下来
    rec = request.urlopen(req)
    # rec = urllib.request.urlopen(request)  # 发送GET请求，获取博客文章页面资源
    page = rec.read()  # 读取页面内容到内存中的变量，这句代码可以不要
    count += 1  # 计数器加1
    print(count)  # 打印当前循环次数
    if count % 6:  # 每6次访问为1个循环，其中5次访问等待时间为31秒，另1次为61秒
        time.sleep(3)  # 为每次页面访问设置等待时间是必须的，
        # 过于频繁的访问会让服务器发现刷阅读量的猥琐行为并停止累计阅读次数
    else:
        time.sleep(4)




