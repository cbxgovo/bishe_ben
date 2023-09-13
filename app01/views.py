# -*- coding: utf-8 -*-
# Create your views here.

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render,redirect
from django.template import loader
import random

import time
import datetime
from datetime import datetime, date

from paho import mqtt
from paho.mqtt import client as mqtt_client
import paho.mqtt.client as mqtt
from app01 import models

#ajax
from django.views.generic.base import View

##########################################################

#首页 可以用于发布命令
def index(request):
     '此视图函数用于示意form表单的提交'

# ****************************************************************
     broker = 'broker.emqx.io'
     port = 1883
     topic = "cc36e70148924ef2bb2e1d477c24675f_shou"
     client_id = f'43f90020d29d491c9e671db1ee5b8db7'

    # 如果是get请求 直接返回页面 返回表单 明面上 输入网页并回车就是GET形式 表单也可以自定义GET/POST
     if request.method == 'GET':
        return render(request, 'index.html')
    # 如果是post请求 获取页面用户提交的数据 form表单提交的数据
     elif request.method == 'POST':

        # 完整打印post的数据
        print(request.POST)

        # 返回表单提交内容的结果
        # dic = dict(request.POST)
        # print("提交的内容是:" , dic)

        # 接收post发送form表单里面input输入框 属性name=num带的值
        canshu = request.POST.get("num")
        canshu1 = request.POST.get("xd1")
        canshu2 = request.POST.get("xd2")
        canshu3 = request.POST.get("xd3")
        print("输入框提交的内容是:", canshu,canshu1,canshu2,canshu3)

        # ****************************************************************
        client = mqtt.Client()
        # client.on_connect = on_connect
        client.connect(broker, port, 60)  # 连接
        client.publish(topic, payload=canshu, qos=0)  # 发布消息
        client.disconnect(broker, port)
        # client.loop_forever()  # 保持连接状态

        return render(request, "index.html", {"name1": canshu})
  




#超声波取样绘制图像 从button3直接复制过来的 
def about(request):
    data = models.Iot.objects.all()
    lenght = data.count()  # 获取表数据总长度
    result = data[lenght - 7:lenght]
    # 定义数两个数组分别存储超声波距离和数据产生的时间
    distance_1 = []
    time_1 = [] # list datetime.datetime类型
    time_1_str = [] # list 2023-04-23 16:22:55类型
    water_1 = []

    # 取数据库的数据存在数组当中
    for obj in result:
        # print(obj.id, obj.dis, obj.create_time,obj.waterdepth)
        distance_1.append(obj.dis)
        time_1.append(obj.create_time)
        water_1.append(str(obj.waterdepth)) # 水位float强制转换为字符型
    # print(type(distance_1)) #list
    # print(type(time_1)) # list
    # print(time_1) # datetime.datetime类型 datetime.datetime(2023, 4, 23, 16, 23, 1, 892467)

    for obj in time_1:
        obj1 = obj.strftime('%Y-%m-%d %H:%M:%S')#只取年月日，时分秒
        time_1_str.append(obj1)
    # print(type(time_1_str)) # lsit
    # print(time_1_str) # 2023-04-23 16:22:55

    # return HttpResponse("插入成功")
    # return render(request, "button3.html", {"button3_distance": distance_1, "button3_time": time_1})
    # return render(request, "button3.html", {"button3_distance": distance_1})
    return render(request, "about.html" , {"button3_distance": distance_1,"button3_time": time_1_str,"button3_water": water_1})

# 图像 摄像头画面 
def work(request):
    broker = 'broker.emqx.io'
    port = 1883
    topic = "cc36e70148924ef2bb2e1d477c24675f_button"# 向该主题发布"1" ,请求识别图像 然后再更新
    client_id = f'43f90020d29d491c9e671db1ee5b8db7'

    client = mqtt.Client()
    # client.on_connect = on_connect
    client.connect(broker, port, 60)  # 连接
    client.publish(topic, payload="2", qos=0)  # 发布消息 不是1就行的else占用
    client.disconnect(broker, port)
    # client.loop_forever()  # 保持连接状态

    # //将存在txt文件的识别信息在网页中显示
    with open('D:\\Desktop\\IOT_SoftWare\\app01\\static\\YoloImages\\yolo.txt', 'r', encoding='utf-8') as f:
        content = f.read()
    return render(request, "work.html", {"work_yolotxt": content})


# GPS定位 请求消息
def contact(request):
    # GPSW = 36.56167324381701
    # GPSJ = 116.80781175110624

    import time
    broker = 'broker.emqx.io'
    port = 1883
    topic = "cc36e70148924ef2bb2e1d477c24675f_gps"
    client_id = f'43f90020d29d491c9e671db1ee5b8db7'
    namegps = '1,2'

    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        global namegps
        global namegps_split_w # 纬度 36
        global namegps_split_j # 经度 116
        namegps = msg.payload.decode()
        client.disconnect(broker, port)
        print("GPS:" + namegps)
        namegps_split = namegps.split(',')
        namegps_split_w = namegps_split[0] #维度
        namegps_split_j = namegps_split[1] #经度
        models.Gps.objects.create(gps_j = namegps_split_j, gps_w = namegps_split_w)

    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(broker, port, 60)
    client.subscribe(topic, qos=0)
    client.loop_forever()
    return render(request, "contact.html", {"weidu": namegps_split_w ,"jingdu":namegps_split_j})

    # 本地测试 松开函数开头的两个本地变量以便于测试
    # return render(request, "contact.html", {"weidu": GPSW ,"jingdu":GPSJ})

# GPS定位 请求消息
def history(request):
    # GPSW = 36.56167324381701
    # GPSJ = 116.80781175110624

    data = models.Gps.objects.all()
    lenght = data.count()  # 获取表数据总长度
    result = data[lenght - 5:lenght]
    # 定义数两个数组分别存储超声波距离和数据产生的时间
    jing = [] # 经度
    wei = [] # 纬度
    time_1 = [] # list datetime.datetime类型
    time_1_str = [] # list 2023-04-23 16:22:55类型
    

    # 取数据库的数据存在数组当中
    for obj in result:
        # print(obj.id, obj.dis, obj.create_time,obj.waterdepth)
        jing.append(obj.gps_j)
        wei.append(str(obj.gps_w)) 
        time_1.append(obj.create_time) # 时间先取出来 但是不用
    # print(type(distance_1)) #list
    # print(type(time_1)) # list
    # print(time_1) # datetime.datetime类型 datetime.datetime(2023, 4, 23, 16, 23, 1, 892467)

    for obj in time_1:
        obj1 = obj.strftime('%Y-%m-%d %H:%M:%S')#只取年月日，时分秒
        time_1_str.append(obj1)
    # print(type(time_1_str)) # lsit
    # print(jing) 
    # print(wei)
    wei0 = wei[0]
    jing0 = jing[0]
    wei1 = wei[1]
    jing1 = jing[1]
    wei2 = wei[2]
    jing2 = jing[2]
    wei3 = wei[3]
    jing3 = jing[3]
    wei4 = wei[4]
    jing4 = jing[4]
    print(wei0)
    return render(request, "history.html", {"weidu0": wei0 ,"jingdu0":jing0,
                                            "weidu1": wei1 ,"jingdu1":jing1,
                                            "weidu2": wei2 ,"jingdu2":jing2,
                                            "weidu3": wei3 ,"jingdu3":jing3,
                                            "weidu4": wei4 ,"jingdu4":jing4 })

 




def information(request):
    return render(request, "information.html", {"information_distance": "1000"})



##########################################################

def panel(request):
    return render(request, "test_form.html")

#发布消息 
def test_form(request):
    '此视图函数用于示意form表单的提交'

# ****************************************************************
    broker = 'broker.emqx.io'
    port = 1883
    topic = "cc36e70148924ef2bb2e1d477c24675f"
    client_id = f'43f90020d29d491c9e671db1ee5b8db7'

    # 如果是get请求 直接返回页面 返回表单 明面上 输入网页并回车就是GET形式 表单也可以自定义GET/POST
    if request.method == 'GET':
        return render(request, 'test_form.html')
    # 如果是post请求 获取页面用户提交的数据 form表单提交的数据
    elif request.method == 'POST':
        # 完整打印post的数据
        print(request.POST)
        # 返回表单提交内容的结果
        # dic = dict(request.POST)
        # print("提交的内容是:" , dic)

        # 接收post发送form表单里面input输入框 属性name=num带的值
        canshu = request.POST.get("num")
        print("输入框提交的内容是:", canshu)

        on = request.POST.get("on")
        print("on提交的内容是:", on)

        off = request.POST.get("off")
        print("off提交的内容是:", off)

        if(on == 1 and (off is None) and (canshu is False)):
            value = 1
        if (on is None and off ==0 ):
            print("on is None and off ==0")
            value = 0
        else:
            print("else")
            value = 0
        print("value:", value)


        # return render(request, "test_form.html", {"name1": canshu})

        # ****************************************************************
        client = mqtt.Client()
        # client.on_connect = on_connect
        client.connect(broker, port, 60)  # 连接
        client.publish(topic, payload=canshu, qos=0)  # 发布消息
        client.disconnect(broker, port)
        # client.loop_forever()  # 保持连接状态

        # return HttpResponse("yes")
        return render(request, "test_form.html", {"name1": canshu})
        # return redirect("https://www.baidu.com")


#ajax静态页面
def  button2_html(request):
    return render(request, "button2.html")


#ajax 局部刷新返回值 包括超声波和水位 只将请求的超声波的数据传入数据库
def button2_fx_view(request):
    import time
    broker = 'broker.emqx.io'
    port = 1883
    topic = "cc36e70148924ef2bb2e1d477c24675f"
    client_id = f'43f90020d29d491c9e671db1ee5b8db7'

    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        # 发布来的消息是 超声波和水位以“10，10.00”形式一起发布,英文逗号分割形成完整字符串发布 即name1
        global name1
        global name1_split_ul
        global name1_split_water
        name1 = msg.payload.decode()
        client.disconnect(broker, port)
        name1_split = name1.split(',') #name1_split 通过数组的方式存放逗号分隔的两个变量
        name1_split_ul = name1_split[0] #超声波 int
        name1_split_water = name1_split[1] #水深 double
        # 存入数据库 以后尝试将时间戳化为字符串存入mysql 不用默认时间戳 
        # 一个数存入 只将超声波或者水深的数据传入数据库
        # models.Iot.objects.create(waterdepth=name1_split_water)
        # 两个数存入 将超声波和水位的数据传入数据库
        models.Iot.objects.create(dis=name1_split_ul,waterdepth=name1_split_water)
        
        print("超声波已经存储"+name1_split_ul+"cm")

        print("水位已经存储"+name1_split_water+"cm")
        

    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    client.connect(broker, port, 60)
    client.subscribe(topic, qos=0)
    client.loop_forever()
    return HttpResponse(name1)



def test_map(request):
    return render(request, "test_map.html")


def button3(request):
    data = models.Iot.objects.all()
    lenght = data.count()  # 获取表数据总长度
    result = data[lenght - 7:lenght]
    # 定义数两个数组分别存储超声波距离和数据产生的时间
    distance_1 = []
    time_1 = []

    for obj in result:
        print(obj.id, obj.dis, obj.create_time)
        distance_1.append(obj.dis)
        time_1.append(obj.create_time)

    print(distance_1[2])
    print(time_1[2])

    # return HttpResponse("插入成功")
    # button3_time无效 可能是因为格式 太复杂 时间戳
    # return render(request, "button3.html", {"button3_distance": distance_1, "button3_time": time_1})
    return render(request, "button3.html", {"button3_distance": distance_1})


##########################################################

#ajax测试 输入网址跳转到该局部刷新的页面
def test_ajax_html(request):
    return render(request, "test_ajax.html")

#ajax测试 请求新网址处理后 调用该网址的处理函数 返回结果填充html 实现局部刷新
def test_ajax(requests):
    n1=int(requests.POST.get('n1'))
    n2=int(requests.POST.get('n2'))
    return HttpResponse(n1+n2)





# def orm(request):
#     # 把数据库的datetime类型转化为字符串类型的库
#     from datetime import datetime

#     # # 1.插入 操作数据库 插入操作
#     # models.Book.objects.create(name="cbxg",price=11)


#     # create_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
#     # print("打印第一行" + create_time)


#     # # 2.删除 filter()是添加筛选条件
#     # models.Book.objects.filter(id=1).delete()
#     # # 删除整张表
#     # # models.Book.objects.all.delete()

#     # # 3.查找 选出来的是一行一行的列表 里面是一个个的对象 比如 x选出来了赋予x for遍历x.age巴拉巴拉的拿出来一列一列的
#     # # data_list = models.Book.objects.filter(id=1)  # 选出id=1的一行 成为一个列表 不能直接打印 for循环打印
#     # data_list = models.Book.objects.filter(id=1).first()
#     # print("打印第一行" + data_list.name + data_list.price)  # 这样可以直接打印第一行

#     # 最后几行筛选测试
#     data = models.Iot.objects.all()
#     lenght = data.count()  # 获取表数据总长度
#     result = data[lenght - 7:lenght]
#     # 定义数两个数组分别存储超声波距离和数据产生的时间
#     distance_1 = []; time_1 = []

#     for obj in result:
#         print(obj.id, obj.dis, obj.create_time)
#         distance_1.append(obj.dis)
#         time_1.append(obj.create_time)
#     # print(distance_1[2])

#         # time_1 = datetime.strptime(time_1, '%Y-%m-%d %H:%M:%S')
#         # time_1_tra = time_1.strftime('%Y-%m-%d %H:%M:%S')


#     # return HttpResponse("插入成功")
#     return render(request, "orm.html", {"distance": distance_1,"time": time_1})

 




