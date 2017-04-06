# -*- encoding:utf-8 -*-

import urllib.request
import re

def request_url(district,  area):
    ##输入查询的区域和小区，返回查询的url
    url_list = []
    if not valid_query_location():
        return (False, None)
    else:
        my_url = "https://sz.lianjia.com/ershoufang/shatoujiao/"
        total_pages = get_total_pages(my_url)
        print(total_pages)
        url_list.append(my_url)
        for i in range(2, total_pages+1):
            new_url = my_url + "pg" + str(i) + "/"
            url_list.append(new_url)
        print(url_list)
        return (True, url_list)

def get_new_url(first_url, page_num):
    url_array = first_url.split("/")
    if url_array[5] == "":
    #url中只包含了地区信息，没有再细分选择
        url_array[5] = "pg" + page_num
    else:
    #url中已经包括了价格、房型以及售价等信息
        url_array[5] = "pg" + page_num + page_num[5]
    #返回新和成的url
    return "/".join(url_array)
    pass

def get_total_pages(first_url):
    total_pages=1
    r = urllib.request.urlopen(first_url)
    data = r.read().decode("utf8")
    m = re.search(r'totalPage":\s*(\d+)', data, re.IGNORECASE)
    if m:
        total_pages = int(m.group(1))
    return total_pages
    #"totalPage":11,

def valid_query_location():
    ##判断输入的查询区域是否合法
    return True

def execute_query(url_list):
    for url in url_list:
        r =  urllib.request.urlopen(url)
        with open("tmp.html", "w", encoding="utf-8") as f:
            f.write(r.read().decode("utf8"))

def main_query():
    area = input("请输入你要查询的地区：")
    flag, url = request_url(area, area)

    if flag:
        execute_query(url)
        pass
    else:
        print("请输入正确的查询条件")

if __name__ == '__main__':
    main_query()


