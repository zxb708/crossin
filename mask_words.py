# -*- coding:utf-8 -*-
#8 - 7.编程实例 - 屏蔽词替换
#【问题描述】

#给定一个屏蔽词列表的文件，文件中每一行都是一个词汇，可能是英文也可能是中文。

#要求：实现一个方法，输入一段文字，将其中存在于列表中的词汇字符替换成 *，返回处理后的文字。

#验证这个方法时，从控制台输入待检测文字，调用方法处理，输出处理后的文字。
#主要涉及内容：文件读取、字符串处理、函数调用

import re
def gen_files():
    with open("words.txt", "w",encoding="utf-8") as f:
        f.write("张小波\n")
        f.write("秋高气爽\n")
        f.write("don't show these words\n")
        f.write("python\n")
        f.write("hard")

def find_mask_words():
    oldstr = instr = input("please enter some words:")
    data = ""
    with open("words.txt",encoding="utf-8") as f:
        data = f.readlines()
    for i in range(len(data)):
        data[i] = data[i].strip()
        instr = re.sub(data[i], '*' * len(data[i]), instr, flags=re.IGNORECASE)
    print("before replace:" + oldstr)
    print("after replace:" + instr)

if __name__ == '__main__':
    gen_files()
    find_mask_words()