---
title: ESP32-CAM 摄像头学习_墨客inkor的博客-CSDN博客
url: https://blog.csdn.net/weixin_45825635/article/details/106081995
clipped_at: 2023-04-11 23:01:26
category: 网页裁剪
tags: 
 - ESP32-CAM
---


# ESP32-CAM 摄像头学习_墨客inkor的博客-CSDN博客

### 目录

*   *   [Arduino环境配置](#Arduino_1)
    *   [硬件连接](#_12)
    *   [程序修改](#_15)

## [Arduino](https://so.csdn.net/so/search?q=Arduino&spm=1001.2101.3001.7020)环境配置

首先我们要先去下载Arduino，大家可以去官网下，也可以在Arduino中文社区进行下载，这是中文社区网址https://www.arduino.cn/。![点进软件下载，里面有大佬分享的Arduino](1681225286.assets/1681225286-a8dbe0d2b1bd92230fd0aba2609bd475.png)  
下载好软件之后，打开软件，点击工具—管理库，搜索[esp32](https://so.csdn.net/so/search?q=esp32&spm=1001.2101.3001.7020)，进行安装![](1681225286.assets/1681225286-cf713ad7baa8d49b11c004669dff6385.png)  
![](1681225286.assets/1681225286-77c76506939aa34004d88c859f2c8b99.png)  
如果没有搜到的话，就转到文件—首选项，将https://dl.espressif.com/dl/package\_esp32\_index.json和http://arduino.[esp8266](https://so.csdn.net/so/search?q=esp8266&spm=1001.2101.3001.7020).com/stable/package\_esp8266com\_index.json添加进去，然后再搜索，应该就能搜到了  
![](1681225286.assets/1681225286-7c59eafdce2c5ad8b6a93cc45d23384c.png)![](1681225286.assets/1681225286-ea57b1103341f0161d2434cab8efeb21.png)  
在安装完库之后，选择工具—开发板，选择如图开发板（可能不一样，根据个人情况进行选择）  
![在这里插入图片描述](1681225286.assets/1681225286-7fe85a1ae275fbd85d25da8a264e714d.png)  
之后再打开文件—示例，找到如图的实例，如果没找到说明库没安装正确  
![在这里插入图片描述](1681225286.assets/1681225286-32bc934fc8f242c76e6ba7ae63946657.png)  
如果你成功的打开了示例，那么就可以进行下一步了。

## 硬件连接

![原图来自网络，侵删](1681225286.assets/1681225286-f70de80de6e779234c62bd06cd17f073.png)  
你可以使用FTDI与ESP32进行连接，如果你手头上没有的话，实测使用USB转TTL也可以正常烧录，需要注意的是烧程序的时候IO0一定要和GND短接，不然无法烧录，烧录结束需要将线移去，这个之后会讲。

## 程序修改

需要修改的地方有两处，第一你需要把CAMERA\_MODEL\_AI\_THINKER宏定义的屏蔽给去掉，把语句前面的//给去掉就行，还有就是你需要将ssid =后面字符串的改为你电脑现在连接的wifi名称，password =后面的改为wifi密码  
![](1681225286.assets/1681225286-8677c0cde776f34939149f8e0824b214.png)  
然后将你的FTDI或者USB转TTl与电脑相连，再点击工具，将设置改为我的设置，注意：你的端口不一定是COM8。  
![](1681225286.assets/1681225286-cd2610a6137eb6fe093fcdda2b788fd1.png)  
然后就可以点击箭头烧程序了，注意：这个时候IO0一定要和GND短接![](1681225286.assets/1681225286-a75ae5d1cc20e0e309df10559001def7.png)  
当出现Connecting时，需要你按一下ESP32上的开关程序才能进行烧录  
![](1681225286.assets/1681225286-3f6c4d584a2b0304b694ddc6d4044c7e.png)  
等待程序烧录完成，将IO0和GND短接的杜邦线取下来，然后打开串口监视器![](1681225286.assets/1681225286-24e0611c07c3be8307840f1740d4fd78.png)  
将波特率设为115200，然后按一下ESP32上的按钮，过一会就会生成IP地址  
![](1681225286.assets/1681225286-e68d846cb6bef6fc4b0699ec8e933294.png)  
进入浏览器，打开地址，点击Start Steam即可看到图像  
![](1681225286.assets/1681225286-1d40b2ac33ffb530ce4510eb517d175b.png)  
在视频传输的过程中，ESP32也会通过串口发送视频帧率等信息，可在串口监视器中查看![](1681225286.assets/1681225286-0b754907c675cc45af1fa1faf3feff0b.png)  
在程序烧录完成后只需连接ESP32的+5V和GND即可进行远程图传