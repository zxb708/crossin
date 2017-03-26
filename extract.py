# -*- coding:utf-8 -*-

import re

def extract_words():
    file_name = "from.txt"
    data_list = []
    pattern = re.compile("[a-zA-Z]+")
    with open(file_name, "r", encoding="utf-8") as f:
        for line in f.readlines():
            data_list.extend(pattern.findall(line))
    data_list.sort()
    with open("to.txt", "w", encoding="utf-8") as f:
        [f.write("%s\n" % x) for x in data_list]

if __name__ == '__main__':
    extract_words()