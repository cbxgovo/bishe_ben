
# 部分命令

版本：0503

> 数据模式更新

python manage.py makemigrations    #将类转换成数据表结构

python manage.py  migrate   #根据上一句代码生成数据表

> 运行指令

python manage.py runserver

> 访问

原首页：http://127.0.0.1:8000/test_form/

首页：http://127.0.0.1:8000/index/


---



# 一、项目简介

本文探讨了基于物联网技术的盲人守护系统的设计与实现，旨在为盲人提供全方位的监控和保护，以帮助其适应环境和提高生活质量。

随着物联网技术的发展，物联网技术已成为了推动社会经济发展、帮助我们更好地掌握信息、提高效率、提升生活质量的重要力量。而盲人群体数量庞大，却相对缺乏为其开发的物联网产品。因此，本文提出了一个基于物联网技术的盲人守护系统，该系统采用多种传感器采集信息，如超声波、光敏电阻、水位、GPS定位等；结合多种技术，如YOLOv5算法、图像识别、语音播报等；使用Django开发系统界面进行数据管理和展示；利用震动模块进行信息反馈和发送邮件主动求助监护人等多种功能。具有实用性和可行性，对于解决盲人生活中的困难和问题具有重要意义。

利用物联网技术实现的盲人守护系统，可以帮助盲人更好地适应复杂的社会环境，提高其独立生活的能力，减少其遭受的损失和伤害，改善盲人的生活质量，提高社会对盲人的关注度，帮助盲人更好地融入社会，提高其社会参与度。

# 二、开发环境

运行环境：python 3.8.15；Django 4.1.7(需要根据python版本查看是否支持进行选择)；

开发工具：Visual Studio Code(推荐)或PyChram、Arduino、SingTownSerialport、MQTT.fx；

操作系统：windows 10；

浏览器：Google Chrome(推荐)、Edge;

数据库：MySQL 5.6.21(推荐)及其他版本（支持，但容易异常尤其MySQL5.7（不含）以下版本）；

数据库可视化工具：Navicat Premium 15（推荐）以及其他Navicat版本

![](项目readme.aasts/image-20230521175755431.png)

Django 版本	Python 版本
2.2	3.5、3.6、3.7、3.8（在 2.2.8 中添加）、3.9（在 2.2.17 中添加）
3.1	3.6、3.7、3.8、3.9（在 3.1.3 中添加）
3.2	3.6、3.7、3.8、3.9、3.10（在 3.2.9 中添加）
4.0、4.1	3.8、3.9、3.10

# 三、项目技术

后端：Flask、PyMySql、paho、OpenCV、yolov5

前端：HTML、Jquery、Ajax、Bootstrap、Echarts

jquery js  、ajax
bootstrap css

# mysql部分cmd命令

mysql -uroot -p 手动输入密码 root0410
mysql -uroot -proot0410  带着密码输入

show databases; 

use test;

show tables;

select * from app01_iot;
select * from app01_iot order by id desc limit 10;

---

吴胜豪数据模式

class temhum(models.Model):
    tem = models.CharField(max_length=20,default=20)
    hum = models.CharField(max_length=20,default=50)
    create_time=models.DateTimeField(auto_now=True)

class ultthree(models.Model):
    ult1 = models.CharField(max_length=20,default=0)
    ult2 = models.CharField(max_length=20,default=0)
    ult3 = models.CharField(max_length=20,default=0)
    create_time=models.DateTimeField(auto_now=True)



李新龙数据模式

class pool(models.Model):
    tem_water = models.FloatField(max_length=20,default=0.00)
    tem_indoors = models.FloatField(max_length=20,default=0.00)
    hum_indoors = models.FloatField(max_length=20,default=0.00)
    qua_water = models.FloatField(max_length=20,default=0.00)
    qua_air = models.FloatField(max_length=20,default=0.00)
    num_person = models.CharField(max_length=20,default=50)
    create_time=models.DateTimeField(auto_now=True) 



# 使用

1. 安装VSCode
   首先，你需要在你的系统上安装VSCode编辑器。你可以在VSCode官方网站上下载，并按照官方指导安装。
2. 安装Python
   Django是一款基于Python开发的Web框架，所以你需要先安装Python。你可以从Python官网上下载需要的版本，并安装到你的系统上。
3. 创建Django项目
   打开终端，进入你想创建项目的目录，输入以下命令来创建你的Django项目：

```
django-admin startproject myproject
```

4. 配置VSCode
   打开VSCode编辑器，打开刚才创建的myproject目录，点击左侧的调试选项卡，然后点击创建“launch.json”文件。在新弹出的窗口中选择“Python”，VSCode将会自动生成“launch.json”文件。
5. 安装扩展
   为了更好的开发体验，你可以在VSCode中安装一些Django扩展，如“Django Snippets”、“Django Template”等等。
6. 启动Django应用程序
   在VSCode中打开“Terminal”，输入以下命令启动Django服务器：

```
python manage.py runserver
```

7. 开始编写代码
   现在你已经完成了Django项目的创建和配置，可以愉快地开始编写代码了！

以上就是使用VSCode开发Django的一些指导。如果你对Django不熟悉，建议你先学习一下Django框架的基础知识。
