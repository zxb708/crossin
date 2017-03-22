# -*- coding:utf-8 -*-

#【项目一】统计成绩
#从成绩单文件 report.txt（点击下载）中读取班级成绩，并完成统计分析。

#姓名 语文 数学 英语 物理 化学 生物 政治 历史 地理
#小A 89 94 90 96 89 92 54 73 80
#小B 92 37 93 43 67 77 82 84 89
#小C 90 88 87 89 82 79 79 80 82

#要求：

#读取 report.txt 文件中的成绩；
#统计每名学生总成绩、计算平均并从高到低重新排名；
#汇总每一科目的平均分和总平均分（见下表第一行）；
#添加名次，替换60分以下的成绩为“不及格”；
#将处理后的成绩另存为一个新文件。

def load_score(file='report.txt'):
    score_list = []
    with open(file,'r',encoding='utf-8') as f:
        for line in f.readlines():
            data = line.split(" ")
            #data = list(data[0]) + [int(x) for x in data[1:]]
            tmp_list = [int(x) for x in data[1:]]
            tmp_list.insert(0, data[0])
            score_list.append(tmp_list)
    return score_list

def cal(score_list):
    avg_list = ["平均"]
    for i in range(10):
        avg_list.append(0)
    stu_num = len(score_list)
    for i in range(stu_num):
        #计算单人成绩的总分和平均分
        sum_score = sum(score_list[i][1:])
        #计算单人成绩的平均分
        avg_score = sum_score/(len(score_list[i]) - 1)
        #添加到列表list中
        score_list[i].append(sum_score)
        score_list[i].append(avg_score)
        for j in range(1, len(avg_list)):
            avg_list[j] += score_list[i][j]


    for i in range(1, len(avg_list)):
        avg_list[i] = avg_list[i] / stu_num
    avg_list.append(avg_list[-1]/9)

    score_list.sort(key=lambda x: x[-1], reverse=True)
    return (score_list, avg_list)

if __name__ == '__main__':
    score_lst = load_score()
    score_lst, avg_lst = cal(score_lst)
    with open("output.txt", "w", encoding="utf-8") as f:
        f.write("名次 姓名 语文 数学 英语 物理 化学 生物 政治 历史 地理 总分 平均分\n")
        #['平均', 69.1, 70.7, 68.53333333333333, 69.6, 72.0, 69.4, 60.43333333333333, 71.0, 2244]
        f.write("0 ")
        f.write("%s " % avg_lst[0])
        for i in range(1, len(avg_lst)):
            f.write("%.1f " % avg_lst[i])
        f.write("\n")
        for i in range(len(score_lst)):
            f.write("%s " % (i+1))
            f.write("%s " % score_lst[i][0])
            for j in range(1,len(score_lst[i]) - 1):
                if score_lst[i][j] < 60:
                    f.write("不及格 ")
                else:
                    f.write("%s " % score_lst[i][j])
            f.write("%.1f\n" % score_lst[i][-1])
