#coding=utf-8
from django import template
import time

#创建模板库的实例
register = template.Library()

#注册过滤器
@register.filter
def dealwithtime(t1):
    x = time.localtime(long(t1)/1000)
    t2 = time.strftime('%Y-%m-%d', x)
    return t2