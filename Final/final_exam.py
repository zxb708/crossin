# -*- coding:utf-8 -*-

from urllib import request
import requests
import re
import threading

def downLoadImages(urlPath, outDir="./"):
    #默认下载到当前目录
    urlList = urlPath.rsplit("/", 1)
    outFile = outDir + urlList[-1]
    #使用request.urlopen方法读取图片
    #然后再用read写入输出文件中
    with request.urlopen(urlPath) as pic:
            with open(outFile, "wb") as outfile:
                outfile.write(pic.read())

if __name__ == '__main__':
    #我们要查询的网站
    queryURL = "http://jandan.net/ooxx/page-"
    pageNum = 1
    #对输入的页面号码进行校验，至少要大于0
    while True:
        try:
            pageNum = int(input("Please input the page number that you want to query:"))
            if pageNum > 0:
                break
        except TypeError as e:
            print(e)
        except:
            pass
    queryURL = queryURL + str(pageNum)

    result = requests.get(queryURL)
    rePattern = r"/\w+.jpg"
    #找出对象中的图片名称
    reList =  re.findall(rePattern, result.text, re.IGNORECASE)
    if len(reList) > 0:
        threads = []
        for filePath in reList:
            #拼接文件地址
            filePath = "http://wx1.sinaimg.cn/mw600" + filePath
            #执行文件下载
            threads.append(threading.Thread(target=downLoadImages, args=(filePath,)))
            #downLoadImages(filePath)
        for t in threads:
            t.setDaemon(True)
            t.start()
        t.join()
        print("Download Finished!")

