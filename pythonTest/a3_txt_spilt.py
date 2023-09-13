    
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

#################################

# print ("数组元素打印")
# for txt_elements in txt:  
#     print (txt_elements)

#################################

message = ""
if txt[0] != 0:# 人
    message = "前方共有"+ str(txt[0]) +"个人,"
if txt[1] != 0: # 自行车
    message = message +  str(txt[1]) +"辆自行车,"
if txt[2] != 0: # 汽车
    message = message +  str(txt[2]) +"辆汽车,"
if txt[3] != 0: # 摩托车
    message = message +  str(txt[3]) +"辆摩托车,"
if txt[4] != 0: # 公共汽车
    message = message +  str(txt[4]) +"辆公共汽车,"
if txt[5] != 0: # 交通灯
    message = message +  str(txt[5]) +"个交通灯,"
if txt[6] != 0: # 长椅
    message = message +  str(txt[6]) +"个长椅,"
if txt[7] != 0: # 狗
    message = message +  str(txt[7]) +"条狗."
print (message)






#   0: 人      a0
#   1: 自行车  a1
#   2: 汽车    a2
#   3: 摩托车  a3
#   5: 公共汽车 a4
#   9: 交通灯   a5
#   13: 长椅   a6
#   16: 狗     a7
