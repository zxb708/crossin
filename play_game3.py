# -*- coding:utf-8 -*-

from random import randint
import os

def gen_num(min_val=1, max_val=100):
    '''
    生成游戏的随机数
    :param min_val:
    :param max_val:
    :return:
    '''
    return randint(min_val, max_val)

def guess_num():
    print("猜猜数字是几？")
    answer = gen_num()
    cnt = 0
    while True:
        guess_val = input("请输入100以内的数字;")
        cnt += 1
        print("第 %s 次" % cnt)
        try:
            guess_val = int(guess_val)
            if guess_val < answer:
                print("太小了\n")
            elif guess_val > answer:
                print("太大了\n")
            else:
                print("猜中了!答案就是%s" % guess_val)
                break
        except:
            pass
    return cnt

def play(username, saved_file = 'guess.dat'):
    new_user = True
    new_user_data = ""
    if os.path.exists(saved_file):
        with open(saved_file, 'r', encoding='utf-8') as f:
            for line in f.readlines():
                if username in line:
                    new_user = False
                    new_user_data = line
                    break
    if not new_user:
        print("欢迎回来 %s ，祝你游戏愉快！" % username)
    else:
        print("欢迎新用户 %s ，祝你游戏愉快！" % username)

    if not new_user:
        data = new_user_data.split()
        reps = int(data[1])
        total_cnt = int(data[2])
        best_cnt = int(data[3])
    else:
        reps, total_cnt, best_cnt = (0, 0, 0)

    mark = False
    while True:

        if mark:
            print("新游戏：")
        cur_cnt = guess_num()
        reps += 1
        total_cnt += cur_cnt
        if best_cnt == 0:
            best_cnt = cur_cnt
        elif best_cnt > cur_cnt:
            best_cnt = cur_cnt

        print("你猜中答案一共用了 %s 次机会" % cur_cnt)
        print("你一共玩了 %s 轮游戏" % reps)
        print("你平均 %s 次猜中答案" % int(total_cnt / reps + 0.5))
        print("你最好成绩是 %s 次" % best_cnt)

        prompt = input("输入\"go\"再玩一次，否则退出游戏！")
        prompt = prompt.strip().lower()
        if prompt != 'go':
            break
        mark = True

    #把数据写入文件
    #第一个玩家
    if not os.path.exists(saved_file):
        with open(saved_file, 'w', encoding='utf-8') as f:
            f.write("%s %s %s %s %s\n" % (username, reps, total_cnt, best_cnt, int(total_cnt/reps + 0.5)))
    else:
        #更新保存数据的文件
        update_saved_file(saved_file, username, reps, total_cnt, best_cnt)

def update_saved_file(saved_file, username, reps, total_cnt, best_cnt):
    old_file = open(saved_file, 'r', encoding='utf-8')
    new_file = open(saved_file + '.update', 'w', encoding='utf-8')

    flag = False
    for line in old_file.readlines():
        data = line.split()
        if len(data) == 5:
            #if data[0].strip() != username:
            if username not in line:
                new_file.write(line)
            else:
                new_file.write("%s %s %s %s %s\n" % (username, reps, total_cnt, best_cnt,  int(total_cnt/reps + 0.5)))
                flag = True
    old_file.close()
    if not flag:
        new_file.write("%s %s %s %s %s\n" % (username, reps, total_cnt, best_cnt, int(total_cnt / reps + 0.5)))
    new_file.close()
    #替换文件
    os.replace(saved_file + ".update",saved_file)

if __name__ == '__main__':
    print("Welcome to play the game!!!")
    username = input("Please enter your nick name:")
    play(username)
    print("Goodbye!!!")
