# -*- coding: utf-8 -*-

#一个猜数字的游戏：程序随机一个结果，用户通过命令行输入去猜。程序会告诉你猜大了还是小了，直到猜中为止。
#游戏可以反复进行，猜中了之后可以重新开始
#统计用户猜了几轮，平均几次猜中
#限制每轮猜的次数，判定输赢

from random import randint
from math import ceil

def gen_num():
    return randint(0, 100)

def play_game():
    print("welcome to enter the game:")
    flag = False
    guess_num = gen_num()
    guess_cnt = 0

    while not flag:
        guess_cnt += 1
        if guess_cnt > 10:
            print("game over. too many times to guess!")
            guess_cnt -= 1
            break
        guess_val = int(input("please enter a integer number:"))

        if guess_val < guess_num:
            print("too small")
        elif guess_val > guess_num:
            print("too large")
        else:
            print("bingo, you are right.")
            flag = True
            break

    return (flag, guess_cnt)


if __name__ == '__main__':
    cycle_cnt = 0
    success_cnt = 0
    total_cnt = 0
    action = "yes"
    while action == "yes":
        cycle_cnt += 1
        ret, cnt = play_game()
        if ret:
            success_cnt += 1
            total_cnt += cnt
        action = input("continue or not(yes/no)")
        action = str(action).lower()

    print("status result:")
    print("you play the game %d times." % cycle_cnt)
    print("average guess cnt of success is %d ." % ceil(total_cnt / success_cnt))

