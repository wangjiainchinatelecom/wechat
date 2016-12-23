# coding:utf8
from django.db import models

# Create your models here.
class csd_message(models.Model):
    status_CHOICES = (
        (1,"待回复"),
        (2,"已回复"),
    )
    customer_id = models.CharField(verbose_name='客户openId',max_length=100)
    opercode = models.IntegerField(verbose_name='消息类型')
    text = models.TextField(verbose_name='消息内容')
    time = models.DateTimeField(verbose_name='消息日期')
    worker = models.CharField(verbose_name='客服编号',max_length=100)
    status = models.IntegerField(verbose_name='状态',default=1)

    class Meta:
        db_table = 'csd_message'
        verbose_name = '客服消息'