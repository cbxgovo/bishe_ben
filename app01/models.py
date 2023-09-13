from django.db import models

# Create your models here.
# python manage.py makemigrations    #将类转换成数据表结构
# python manage.py  migrate   #根据上一句代码生成数据表

# 类名相当于表名 【app01_book】 name啥的相当于列名 还会自动创建一列id
class Book(models.Model):
    name = models.CharField(max_length=20)
    price = models.IntegerField()


class Iot(models.Model):
    dis = models.CharField(max_length=20)
    waterdepth = models.FloatField(max_length=20,default=0.00)
    create_time=models.DateTimeField(auto_now=True) #创建时间

class Gps(models.Model):
    gps_j = models.CharField(max_length=20,default=116.811379)
    gps_w = models.CharField(max_length=20,default=36.556447)
    create_time=models.DateTimeField(auto_now=True) #创建时间

# class temhum(models.Model):
#     tem = models.CharField(max_length=20,default=20)
#     hum = models.CharField(max_length=20,default=50)
#     create_time=models.DateTimeField(auto_now=True) 


# class ultthree(models.Model):
#     ult1 = models.CharField(max_length=20,default=0)
#     ult2 = models.CharField(max_length=20,default=0)
#     ult3 = models.CharField(max_length=20,default=0)
#     create_time=models.DateTimeField(auto_now=True) 