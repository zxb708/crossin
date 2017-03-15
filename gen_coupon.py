# -*- coding:utf-8 -*-

#【问题描述】

#很多付费应用的开发者，会设计一些优惠券来吸引用户来使用新开发的应用，以达到一定的广告效应。

#现在，请你帮他们设计并生成200个优惠券号码：

#可以是26个英文字符（大小写）
#可以是8位的优惠券号码

from random import randint

def gen_coupon(num=10, length=8):
    lst = []
    src = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    cnt = 0
    while cnt < num:
        myseq = ''.join([ src[randint(0, len(src)-1)] for i in range(int(length))])
        if myseq not in lst:
            lst.append(myseq)
            cnt += 1
    return lst

if __name__ == '__main__':
    rlst = gen_coupon(200, 8)
    for seq in rlst:
        print(seq)