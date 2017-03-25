# -*- coding:utf-8 -*-

import os
import datetime

def get_input_value(prompt="请输入参数值",func = float):
    input_value = -1
    while True:
        input_value = input(prompt)
        try:
            input_value = input_value.strip()
            input_value = func(input_value)
        except:
            print("请输入合适的值！")
            continue
        break
    #返回获取到的输入值
    return input_value

def query_bill():
    print("查账模式")
    print("1.查询最近十笔交易记录")
    print("2.查询与某公司交易往来")
    print("3.查询最近资产负债状况")

    service_type = "0"
    while True:
        service_type = input("请选择服务：")
        if service_type == "1" or service_type == "2" or service_type == "3":
            break

    if service_type == "1":
        quey_recent_ten_records()
    elif service_type == "2":
        company = input("请输入公司名：")
        query_company_details(company)
    else:
        query_loadbalance()

def quey_recent_ten_records():
    account_detail = "account.txt"
    print("最近十笔交易")
    data_list = []
    with open(account_detail, "r", encoding="utf-8") as f:
        for line in f.readlines():
            data_list.append(line)
            if len(data_list) > 11:
                data_list.pop(0)

    [print(x) for x in data_list]

def query_company_details(company):
    account_detail = "account.txt"
    data_list = []
    count = 0
    with open(account_detail, "r", encoding="utf-8") as f:
        for line in f.readlines():
            if company in line:
                count += 1
                data_list.append(line)
    print("与%s共有%s笔交易" % (company, count))
    for elem in data_list:
        display(elem)

def display(elem):
    data = elem.split("\t")
    print("交易时间：%s" % data[5])
    print("收入：%s" % data[1])
    print("支出：%s" % data[2])
    print("应收账款：%s" % data[3])
    print("应出账款：%s" % data[4])
    print()

def query_loadbalance():
    balance_file="balance.txt"
    data = ""
    first_flag = True
    with open(balance_file, "r", encoding="utf-8") as f:
        for line in f.readlines():
            if first_flag == True:
                first_flag = False
                continue
            data = line.rstrip("\n")
            #print(data)
    if data == "0":
        print("No data in balance file.")
    else:
        balance_list = data.split("\t")
        print("最新资产：%s" % balance_list[1])
        print("最新负债：%s" % balance_list[2])
        print("最新净资产：%s" % balance_list[3])
        print("最后更新日期：%s" % balance_list[0])

def update_bill():
    print("记账开始")
    print("记账模式")
    company = input("交易对象：")
    income = get_input_value("收入/万：")
    pay = get_input_value("支出/万：")
    wait_income = get_input_value("应收账款/万：")
    wait_pay = get_input_value("应出账款/万：")

    #print("%s\t%s\t%s\t%s\n"% (income, pay, wait_income, wait_pay))
    balance, debt = load_balance_data()
    new_balance = float(balance) + income - pay
    new_debt = float(debt) + wait_pay - wait_income
    net_asset = new_balance - new_debt
    ##记录每笔交易的流水
    write_account_detail(company, income, pay, wait_income, wait_pay)
    #自动更新资产负债表
    write_balance_detail(new_balance, new_debt)
    print()
    print("交易已记录")
    print("当前资产状况：")
    print("最新资产：%s 万" % int(new_balance))
    print("最新负债：%s 万" % int(new_debt))
    print("最新净资产：%s 万" % int(new_balance - new_debt))
    ##print("%s\t%s\n" % (balance, debt))

def write_balance_detail(balance, debt):
    balance_file = "balance.txt"
    with open(balance_file, "a", encoding="utf-8") as f:
        #cur_date = datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d %H:%M:%S")
        cur_date = datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d")
        f.write("%s\t%s\t%s\t%s\n" % (cur_date, balance, debt, balance - debt))

def write_account_detail(company, income, pay, wait_income, wait_pay):
    account_detail = "account.txt"
    if not os.path.exists(account_detail):
        with open(account_detail, "w", encoding="utf-8") as f:
            f.write("交易对象\t收入/W\t支出/W\t应收账款/W\t应出账款/W\t交易日期\n")
    with open(account_detail, "a", encoding="utf-8") as f:
        cur_date = datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d")
        f.write("%s\t%s\t%s\t%s\t%s\t%s\n" % (company, income, pay, wait_income, wait_pay, cur_date))

def load_balance_data():
    balance_file = "balance.txt"
    cur_balance, cur_debt = (0, 0)
    cur_date = datetime.datetime.strftime(datetime.datetime.now(), "%Y-%m-%d")
    if not os.path.exists(balance_file):
        with open(balance_file, "w", encoding="utf-8") as f:
            f.write("结算日期\t资产/W\t负债/W\t净资产/W\n")
            f.write("%s\t%s\t%s\t%s\n" % (cur_date, cur_balance, cur_debt, cur_balance-cur_debt))
    else:
        with open(balance_file, "r", encoding="utf-8") as f:
            data = f.readline()
            for line in f.readlines():
                data = line
            data_list = data.split("\t")
            cur_balance = data_list[1]
            cur_debt = data_list[2]
    return cur_balance, cur_debt

    return cur_balance, cur_debt

def main():
    print("1.查账；2.记账")

    service_id = "0"
    while True:
        service_id = input("请选择服务：")
        service_id = service_id.strip()
        if service_id == "1" or service_id == "2":
            break
        else:
            print("请输入正确的服务类型（1 or 2）")
    if service_id == "1":
        #查账逻辑
        query_bill()
    else:
        #记账过程
        update_bill()

if __name__ == '__main__':
    main()