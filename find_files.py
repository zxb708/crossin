#【问题描述】

#用 Python 做运维或写自动化脚本时，难免要和文件打交道。
#要求：输入关键字，列出指定文件夹中的所有文件名中含有此关键字的文件，以及文件内容中含有此关键字的文件。

# -*- coding:utf-8 -*-

import os
import re
def find_files(find_path=r"D:\2017\crossin", core_key="test"):
    #定义的函数
    #参数为路径和关键字
    #返回值为一个list
    #如果list为空，则表示没有找到匹配的文件
    #否则对应匹配的文件列表
    re_list = []
    for root, dirs, files in os.walk(find_path):
        for name in files:
            pattern = core_key
            file_path = root + os.sep + name
            #if re.search(pattern, file_path):
            if name.find(pattern) != -1:
                re_list.append(file_path)
            else:
                with open(file_path, "r", encoding="utf-8") as f:
                    try:
                        #if re.search(pattern, f.readlines()):
                        for l in f.readlines():
                            if pattern in l:
                                re_list.append(file_path)
                                break
                    except:
                        pass
    #返回值
    return  re_list

if __name__ == '__main__':
    dst = input("please enter the dir:")
    search_key = input("please enter the key word:")

    saved_list = find_files(dst, search_key)
    count = 0
    for file in saved_list:
        count += 1
        print(file)
    print("There are %d files matched." % count)