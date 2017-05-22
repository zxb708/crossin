# -*- coding:utf-8 -*-

import sqlite3
#请选择：1.录入 2.查找 3.全部显示 4.删除 (回车退出)
#1
#姓名：张三
#手机：13023323233
#邮箱：zhang3@crossin.me
#联系人保存成功。

#请选择：1.录入 2.查找 3.全部显示 4.删除 (回车退出)
#2
#查询关键字：233
#1 二狗子 13045613243 doge233@163.com
#3 张三 13023323233 zhang3@crossin.me

#请选择：1.录入 2.查找 3.全部显示 4.删除 (回车退出)
#3
#1 二狗子 13045613243 doge233@163.com
#2 陈大喵 18900662001 miao@qq.com
#3 张三 13023323233 zhang3@crossin.me

#请选择：1.录入 2.查找 3.全部显示 4.删除 (回车退出)
#4
#联系人ID：1
#1 二狗子 13045613243 doge233@163.com
#确认删除此联系人？(y/[n])y
#删除联系人成功。


def init_data():
    conn = sqlite3.connect("test.db")

    print("Open database successfully")

    table_exists = False
    try:
        conn.execute('''CREATE TABLE CONTACT
           (ID INTEGER PRIMARY KEY AUTOINCREMENT,
           NAME           TEXT    NOT NULL,
           PHONE          TEXT    NOT NULL,
           EMAIL          CHAR(50));''')
    except:
        table_exists = True
        pass
    if table_exists:
        print("Table already exists")
    else:
        print("Table created successfully")
    return conn

def insert_data(conn):
    name = input("enter your name:")
    phone = input("enter your phone:")
    email = input("enter your email:")

    conn.execute("INSERT INTO CONTACT (NAME,PHONE,EMAIL) \
          VALUES ('%s', '%s', '%s')" % (name, phone, email))

    #提交，把数据写入数据库中
    conn.commit()

def select_data(conn):
    keywords = input("查询关键字：")
    cursor = conn.execute("SELECT * from CONTACT where NAME like '%%%s%%' or PHONE like '%%%s%%' or email like '%s'" % (keywords, keywords, keywords))
    for result in cursor:
        print("# " + " ".join([str(x) for x in result]))

def display_data(conn):
    cursor = conn.execute("SELECT * FROM CONTACT;")
    for result in cursor:
        print("# " + " ".join([str(x) for x in result]))

def delete_data(conn):
    contact_id = input("联系人ID：")
    cursor = conn.execute("select * from CONTACT where ID = %s" % (contact_id,))
    for result in cursor:
        print("# " + " ".join([str(x) for x in result]))
    confirm = input("确认删除此联系人？(y/n)")
    if confirm == 'y':
        conn.execute("delete from CONTACT where id = %s" % (contact_id,))
        conn.commit()
        print("删除联系人成功。")

def main():

    conn = init_data();
    while True:
        choice = input("请选择：1.录入 2.查找 3.全部显示 4.删除 (回车退出)")
        try:
            choice = int(choice)
        except ValueError:
            pass

        #获得了输入值，通过判断开始处理
        if choice == 1:
            insert_data(conn)
        elif choice == 2:
            select_data(conn)
        elif choice == 3:
            display_data(conn)
        elif choice == 4:
            delete_data(conn)
        else:
            break

    conn.close()
    print("再见，欢迎下次使用。")
if __name__ == '__main__':
    main()