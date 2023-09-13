# mqtt持续监听 并检测到特定信息后向指定的主题发送信息
# 2023.04.16 created by 徐梦昊
# python3.6
# -*- coding: utf-8 -*-
import paho.mqtt.client as mqtt
import random


broker = 'broker.emqx.io'
port = 1883
topic_button = "cc36e70148924ef2bb2e1d477c24675f_button"
topic_mp3 = "cc36e70148924ef2bb2e1d477c24675f_mp3"
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
        # 订阅
        client.subscribe(topic_button)
 
 
    def on_message(self, client, userdata, msg):
        print("on_message topic:" + msg.topic + " message:" + str(msg.payload.decode('utf-8')))
        strmqtt = str(msg.payload.decode('utf-8'))
        if strmqtt == "1":
            print("接收到按键请求 请求发布画面识别的语音播报")
            publish()
        else:
            print("未收到正确按键请求 占空用")
        
 
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

    client.publish(topic_mp3, payload='前方共有1个人 3辆汽车 1条狗 ', qos=0, retain=False)

 
if __name__ == '__main__':
    MqttRoad(broker, 1883, 600)


