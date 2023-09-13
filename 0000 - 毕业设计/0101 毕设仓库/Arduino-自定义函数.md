---
title: Arduino 自定义函数
url: https://blog.csdn.net/weixin_45853406/article/details/115269771
clipped_at: 2023-04-20 22:06:53
category: 网页裁剪
tags: 

---


# Arduino 自定义函数

## 函数

就是你把一些动作打包，这个动作可以理解为实现方法。  
比如我想输出某些字符串；  
比如我想输出两个数的积；  
比如我想控制LED灯亮灭；  
比如我想输出计算值；  
函数就是把相同的动作打包，从而减少重复代码量。

## 无参无返回值

```c
void setup() {
  Serial.begin(9600);
  show();
}

void loop() {
}

void show(){
  Serial.println("无参无返回值");
}
```

串口输出：无参无返回值

## 无参有返回值

```c
void setup() {
  Serial.begin(9600);
  Serial.println(show());
}

void loop() {
}

int show(){
  int z;
  int x=10;
  int y=10;
  z = x*y;
  return z;
}
```

串口输出：100

## 有参无返回值

```c
int LED = 13;
void setup() {
  Serial.begin(9600);
  pinMode(LED,OUTPUT);
}

void loop() {
  show(1000);
}

void show(int x){
  digitalWrite(LED,HIGH);
  delay(x);
  digitalWrite(LED,LOW);
  delay(x);
}
```

LED灯：亮1秒，灭1秒

## 有参有返回值

```c
void setup() {
  Serial.begin(9600);
  Serial.println(show(10));
}

void loop() {
}

int show(int x){
  int y;
  y = x+10;
  return y;
}
```

串口输出：20

文章知识点与官方知识档案匹配，可进一步学习相关知识

[C技能树](https://edu.csdn.net/skill/c/c-e2785c48975d4b32917e89a5c260ae27?utm_source=csdn_ai_skill_tree_blog)[函数与程序结构](https://edu.csdn.net/skill/c/c-e2785c48975d4b32917e89a5c260ae27?utm_source=csdn_ai_skill_tree_blog)[函数的声明与定义](https://edu.csdn.net/skill/c/c-e2785c48975d4b32917e89a5c260ae27?utm_source=csdn_ai_skill_tree_blog)142756 人正在系统学习中