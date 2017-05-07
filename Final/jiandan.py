# -*- coding:utf-8 -*-

from urllib import request
import requests
import re
import threading

def downLoadImages(urlPath, outDir="./"):

    urlList = urlPath.rsplit("/", 1)
    outFile = outDir + urlList[-1]

    with request.urlopen(urlPath) as pic:
            with open(outFile, "wb") as outfile:
                outfile.write(pic.read())
                print("%s 下载完成" % (urlList[-1]))

if __name__ == '__main__':

    queryURL = "http://jandan.net/ooxx/page-"
    pageStartNum = 1

    while True:
        try:
            #pageNum = int(input("Please input the page number that you want to query:"))
            pageStartNum = int(input("请输入起始页："))
            pageEndNum = int(input("请输入终止页："))
            if pageEndNum - pageStartNum  >= 0:
                break
        except TypeError as e:
            print(e)
        except:
            pass
    queryList = [queryURL + str(pageStartNum)]
    for i in range(pageEndNum - pageStartNum):
        queryList.append(queryURL + str(pageStartNum+1))
    print("开始下载")

    threads = []
    download_list = []
    for page in queryList:
        result = requests.get(page)
        rePattern = r"/\w+.jpg"

        reList =  re.findall(rePattern, result.text, re.IGNORECASE)
        if len(reList) > 0:

            for filePath in reList:

                filePath = "http://wx1.sinaimg.cn/mw600" + filePath
                if filePath not in download_list:
                    download_list.append(filePath)
                    threads.append(threading.Thread(target=downLoadImages, args=(filePath,)))
                    #downLoadImages(filePath)
    #

    for t in threads:
        t.setDaemon(True)
        t.start()
    t.join()

    while True:
        pass