# -*- coding:utf-8 -*-

from random import randint
import os

def gen_num(min_val=0, max_val=100):
    '''
    生成游戏的随机数
    :param min_val:
    :param max_val:
    :return:
    '''
    return randint(min_val, max_val)

def guess_num():
    answer = gen_num()
    cnt = 0
    while True:
        guess_val = input("please guess the number;")
        try:
            guess_val = int(guess_val)
            if guess_val < answer:
                print("too small")
            elif guess_val > answer:
                print("too big")
            else:
                print("right")
                break
            cnt += 1
        except:
            pass
    return cnt

def play(username, saved_file = 'guess.dat'):
    reps = 0
    total_cnt = 0

    while True:
        cur_cnt = guess_num()
        reps += 1
        total_cnt += cur_cnt
        prompt = input("do you want to play again?(yes/no)")
        prompt = prompt.strip().lower()

        while prompt != 'no' and prompt != 'yes':
            prompt = input("do you want to play again?(yes/no)")
            prompt = prompt.strip().lower()
        if prompt == 'no':
            break

    #把数据写入文件
    #第一个玩家
    if not os.path.exists(saved_file):
        with open(saved_file, 'w', encoding='utf-8') as f:
            f.write("%s %s %s\n" % (username, reps, int(total_cnt/reps + 0.5)))
    else:
        #更新保存数据的文件
        update_saved_file(saved_file, username, reps, total_cnt)

def update_saved_file(saved_file, username, reps, total_cnt):
    old_file = open(saved_file, 'r', encoding='utf-8')
    new_file = open(saved_file + '.update', 'w', encoding='utf-8')

    flag = False
    for line in old_file.readlines():
        data = line.split()
        if len(data) == 3:
            if data[0].strip() != username:
                new_file.write(line)
            else:
                old_reps = int(data[1])
                old_avg = int(data[2])

                new_reps, new_avg = old_reps+reps, int((total_cnt + old_reps*old_avg) / (old_reps + reps) + 0.5)
                new_file.write("%s %s %s\n" % (username, new_reps, new_avg))
                flag = True
    old_file.close()
    if not flag:
        new_file.write("%s %s %s\n" % (username, reps, int(total_cnt / reps + 0.5)))
    new_file.close()
    #替换文件
    os.replace(saved_file + ".update", saved_file)

if __name__ == '__main__':
    print("Welcome to play the game!!!")
    while True:
        username = input("Please enter your nick name:")
        play(username)
        #询问是否再玩下一轮
        prompt = input("do you want to switch user and play again(yes/no)")
        prompt = prompt.strip().lower()
        while prompt != 'yes' and prompt != 'no':
            prompt = input("do you want to switch user and play again(yes/no)")
        if prompt == "no":
            break

    print("Goodbye!!!")
