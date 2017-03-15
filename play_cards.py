# -*- coding:utf-8 -*-
#7-16. 编程实例 - 三人斗地主手牌生成
#

#三人斗地主手牌规则：

#一副牌54张（4种花色各13张，大小王），一人17张，留3张做底牌。
#要求：
#
#将一副牌随机打乱（洗牌）后分配给3位玩家（发牌），输出每个人的手牌和剩余底牌。
#可使用list和random完成。

from random import shuffle
from random import randint

def show_cards():
    lst = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
    alst = []
    alst.extend(["黑桃-" + str(i) for i in lst])
    alst.extend(["红桃-" + str(i) for i in lst])
    alst.extend(["樱花-" + str(i) for i in lst])
    alst.extend(["方块-" + str(i) for i in lst])
    alst.extend(["大王", "小王"])

    shuffle(alst)

    p1 = []
    p2 = []
    p3 = []
    left = []
    for i in range(17):
        index = randint(0, len(alst)-1)
        p1.append(alst.pop(index))
        index = randint(0, len(alst)-1)
        p2.append(alst.pop(index))
        index = randint(0, len(alst)-1)
        p3.append(alst.pop(index))
    print(alst)
    left = alst[:]
    p1.sort()
    p2.sort()
    p3.sort()
    left.sort()
    print("玩家A的牌:" + ",".join(p1))
    print("玩家B的牌:" + ",".join(p2))
    print("玩家C的牌:" + ",".join(p3))
    print("底牌:" + ",".join(left))


if __name__ == '__main__':
    show_cards()