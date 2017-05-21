# -*- coding:utf-8 -*-

#【问题描述】

#用 python 来获取某个城市的天气情况。
#已知有这样一个接口：
#http://wthrcdn.etouch.cn/weather_mini?city=北京
#可以返回 city 对应城市的天气情况，返回数据为 json 格式。
#需注意的是，在实际使用中发现，返回结果有可能会被使用 gzip 压缩，直接显示的话会是乱码。
#参考文章：查天气（http://bbs.crossincode.com/forum.php?mod=viewthread&tid=8）
#要求：在控制台输入一个城市名称，输出此城市当前的天气情况。
#主要涉及内容：输入输出、网络请求、json、字典、gzip、requests

import requests
import urllib.parse
import json


def query_weather(city):

    query_city = urllib.parse.quote(city)
    query_url = "http://wthrcdn.etouch.cn/weather_mini?city=" + query_city

    ret_obj = requests.get(query_url)
    ret_list = json.loads(ret_obj.text)

    data = ret_list["data"]["forecast"]

    print("城市：%s， 天气预报" %  (city,))
    for tmp in data:
        print("日期：%s" % tmp['date'])
        print("高温：%s" % tmp['high'])
        print("低温：%s" % tmp['low'])
        print("天气：%s" % tmp['type'])

if __name__ == '__main__':
    query_weather("北京")