#【问题描述】
#奥运会期间，奖牌榜备受关注。奖牌榜上的信息每天都在更新。

#要求：运用面向对象的知识，构造一个类来描述每个国家的奖牌情况。
#类的属性包括：国家名、金银铜牌数量
#再提供方法：新增奖牌、输出奖牌榜信息、获取奖牌总数等

#分别按金牌数和奖牌总数对奖牌榜列表进行排序

class GoldMedal(object):

    def __init__(self, countryName, goldNum=0, silverNum=0, bronzeNum=0):
        self.goldNum = goldNum
        self.silverNum = silverNum
        self.bronzeNum = bronzeNum
        self.countryName = countryName

    #增加奖牌的方法
    #根据medal_type 参数指定奖牌类型 1：金牌 2：银牌 3：铜牌
    def add_medal(self, medal_type, num):
        if num < 0:
            raise TypeError
        if medal_type == 1:
            self.goldNum += num
        elif medal_type == 2:
            self.silverNum += num
        elif medal_type == 3:
            self.bronzeNum += num
        else:
            pass

    def sum_medal(self):
        return self.goldNum + self.silverNum + self.bronzeNum

    def get_gold_medal(self):
        return self.goldNum
    def get_silverNum(self):
        return self.silverNum
    def get_bronzeNum(self):
        return self.bronzeNum

    def print_medal_info(self):
        #print("Country: %s\nGold Medal:%s\nSilver Medal:%s\nBronze Medal:%s\n" %
        #      (self.countryName, self.goldNum, self.silverNum, self.bronzeNum))
        return [self.goldNum, self.silverNum, self.bronzeNum]

    def __str__(self):
        return ("Country: %s\nTotal Medal:%s\nGold Medal:%s\nSilver Medal:%s\nBronze Medal:%s\n" %
              (self.countryName, self.goldNum + self.silverNum + self.bronzeNum, self.goldNum, self.silverNum, self.bronzeNum))


if __name__ == '__main__':

    clist = []
    c1 = GoldMedal("China", 50, 40, 30)
    clist.append(c1)

    c2 = GoldMedal("India", 10, 20, 30)
    clist.append(c2)
    c1.add_medal(1, 2)
    c1.add_medal(2, 4)
    c2.add_medal(2, 5)
    c3 = GoldMedal("America", 30, 50, 50)

    clist.append(c3)
    clist.sort(key = lambda  x : x.sum_medal(), reverse=True)

    print("-----------------------------------------------------------------------")
    print("after first sort by sum of medals:")
    for e in clist:
        print(e)

    print("=======================================================================")
    print("after first sort by number of gold medals:")
    clist.sort(key = lambda  x : x.get_gold_medal(), reverse=True)

    for e in clist:
        print(e)







