#【问题描述】
#打印自己的英文昵称
#打印一个含有加减乘除的数学表达式
#使用两次 print 语句，但只显示一行
#使用一次 print 语句，但显示在两行中

#NameError: name 'func1' is not defined
def func1():
    print("my name is ws")

def func2():
    print("1 + 2 * 3 - 4 / 3 =", 1 + 2 * 3 - 4 / 3)
def func3():
    print("first line", end=" ")
    print("second line.")

def func4():
    print("this is first line", "this is second line", sep="\n")

if __name__ == '__main__':
    func1()
    func2()
    func3()
    func4()

