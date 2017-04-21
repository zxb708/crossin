# -*- encoding:utf-8 -*-

#【问题描述】
#高考英语作文，规定了学生写满100个单词的作文。
#现在，对于任一个英文的纯文本文件，请统计其中的单词出现的个数。

import re

def count_file_words(article_file):
    with open(article_file) as f:
        content = f.read()
        print("content:%s" % content)
        words = re.findall(r"\b[-\w]+\b", content)
        print(words)
        return len(words)

if __name__ == '__main__':
    filename = input("请输入你要统计的文件：")
    print("文件：%s 有%s个单词！" % (filename, count_file_words(filename)))
