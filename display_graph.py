# -*- coding:utf-8 -*-
#6-11. 编程实例 - 打印图形
#【问题描述】

#用符号的组合在控制台输出不同大小的矩形图案。

#要求：写一个输出矩形的函数，该函数拥有三个默认参数，矩形的长5、宽5和组成图形的点的符号“*”，为函数添加不同的参数，输出三个不同类型的矩形；

#结果示例：

def print_rect(height, width, sign="*"):
    graph = sign * width + "\n"
    print (graph * height, end="")

if __name__ == '__main__':
    print_rect(5, 5)
    print_rect(4, 3)
    print_rect(2, 6, "!")