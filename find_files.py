#【问题描述】

#用 Python 做运维或写自动化脚本时，难免要和文件打交道。
#要求：输入关键字，列出指定文件夹中的所有文件名中含有此关键字的文件，以及文件内容中含有此关键字的文件。

# -*- coding:utf-8 -*-

import os
import re
def find_files(find_path="D:\\2017\\crossin", core_key="test"):
    #定义的函数
    #参数为路径和关键字
    #返回值为一个list和布尔值组成的tuple
    re_list = []
    re_flag = False
    for root, dirs, files in os.walk(find_path):
        for name in files:
            pattern = core_key
            file_path = root + os.sep + name
            if name == "find_files.py":
                print("hello file:" + name)
            if re.search(pattern, file_path):
                re_list.append(root + os.sep + name)
                re_flag = True
            else:
                with open(file_path, "r") as f:
                    if re.search("find_files.py", file_path):
                        print("test")
                    try:
                        if re.search(pattern, f.read().encode("cp936")):
                            re_list.append(file_path)
                            re_flag = True
                    except:
                        pass

    for file in re_list:
        print(str(file))
    #返回值
    return (re_list, re_flag)

if __name__ == '__main__':
    dst = input("please enter the dir:")
    search_key = input("please enter the key word:")

    saved_list, ret_flag = find_files(dst, search_key)
    if ret_flag:
        for file in saved_list:
            print(file)
    else:
        print("No files found.")