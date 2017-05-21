# -*- coding:utf-8 -*-

#【问题描述】
#很多付费应用的开发者，会设计一些优惠券来吸引用户来使用新开发的应用，以达到一定的广告效应。
#现在，请你帮他们设计并生成200个优惠券号码：
#可以是26个英文字符（大小写）
#可以是8位的优惠券号码

import random

def gen_code(code_list, length):
    re_str = ""
    code_len = len(code_list)

    times = 0
    while times < length:
        idx = random.randint(0, code_len - 1)
        re_str += str(code_list[idx])
        times += 1
    return re_str

def main():
    sList =  [chr(x) for x in range(ord('a'), ord('z') + 1)]
    dList = [chr(x) for x in range(ord('A'), ord('Z') + 1)]
    dList = list(range(0, 10))
    sList.extend(dList)
    count = 0
    result = []
    while count < 200:
        count += 1
        tmp = gen_code(sList, 8)
        #判断优惠码是否重复，重复则继续生成直到不重复为止
        while tmp in result:
            tmp = gen_code(sList, 8)
        result.append(tmp)

    count = 1
    for code in result:
        print("第%s个优惠码：%s" % (count, code,))
        count += 1
if __name__ == '__main__':
    main()