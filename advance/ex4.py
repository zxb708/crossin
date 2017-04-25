# -*- coding:utf-8 -*-

#简单的绩点计算器
#难度：
#【问题描述】

#要求：依次输入每门课程的分数与学分，最终得到平均绩点

#平均绩点的计算公式：
# (课程学分1 * 绩点 + 课程学分2 * 绩点 + ...... + 课程学分n * 绩点) / (课程学分1 + 课程学分2 + ...... + 课程学分n)

def get_jidian(score):
    #根据输入成绩计算绩点
    re = 0
    if score > 89:
        re = 4
    elif score > 84:
        re = 3.7
    elif score > 81:
        re = 3.3
    elif score > 77:
        re = 3
    elif score > 74:
        re = 2.7
    elif score > 70:
        re = 2.3
    elif score > 65:
        re = 2
    elif score > 61:
        re = 1.7
    elif score > 59:
        re = 1.3
    else:
        re = 0
    return re

def convert_re(list):
    return sum([sub_list[0]*sub_list[1] for sub_list in list]) / sum([sub_list[1] for sub_list in list])


if __name__ == '__main__':
    data_list = []
    while True:
        course = input("课程名称：")
        score = float(input("请输入成绩："))
        xuefen = float(input("请输入学分："))
        data_list.append([get_jidian(score), xuefen])

        prompt = input("do you want to continue:(yes/no)")
        prompt = prompt.strip().lower()
        if prompt == 'no':
            break

    print("the average value is {}.".format(convert_re(data_list)))