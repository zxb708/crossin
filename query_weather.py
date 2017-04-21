# -*- encoding:utf-8 -*-


import urllib.parse
import requests
import json


def query_city_weather(city):
    #print("The weather of the city:" + city)
    city = urllib.parse.quote(city)
    url = "http://wthrcdn.etouch.cn/weather_mini?city=" + city
    #req = urllib.request.urlopen(url)
    req = requests.get(url=url)
    #print(req.status_code)
    query_ret = req.text
    weather_dict = json.loads(query_ret)
    print_weather_info(weather_dict)

def print_weather_info(mydict):
    #{"desc":"invilad-citykey","status":1002}
    #"desc":"OK","status":1000
    if mydict['status'] == 1000:
        weather_info = mydict['data']
        today = weather_info["forecast"][0]
        print("%s今日天气：%s，最低温度%s, 最高温度%s。" % (weather_info["city"], today["type"], today["low"], today["high"]))
    else:
        print("query result is not ok. desc:" + mydict["desc"])

def valid_city(city):
    if city.strip() == "":
        return False
    return True

if __name__ == '__main__':
    while True:
        city = input("请输入你要查询的城市：")
        query_city_weather(city)
        choose = input("query again?(yes/no)")
        choose = choose.lower()
        if choose.find("no") != -1:
            # 如果输入的字符中没有包含no
            break
