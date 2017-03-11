# -*- coding:utf-8 -*-

from functools import reduce

def func(n):
    rList = [i for i in range(11111,999999+1) if str(i)[::-1] == str(i) \
                and reduce(lambda x,y:int(x)+int(y),list(str(i)))== n]
    for l in rList:
        print(l)

if __name__ == '__main__':
    inValue=int(input("please input a integer number(5<=n<=54):"))
    while inValue < 5 or inValue > 54:
        inValue=int(input("please input a integer number(5<=n<=54):"))
    func(inValue)