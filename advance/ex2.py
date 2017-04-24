#【问题描述】
#想一下以下变量分别是什么。输出结果，看看是否符合你的判断。
#a = 'hello,world'
#b = 1.414
#c = (1 != 2)
#d = (True and False)
#e = (True or False)
#通过字符串格式化在同一行输出 a，b，c，d，e，其中浮点数要求只保留两位小数。输出示例：
#a:hello,word; b:1.41; c:True; d:False; e:True
#定义一个字符串，使其输出结果如下图所示
#d = (True and False)
#e = (True or False)
#通过字符串格式化在同一行输出 a，b，c，d，e，其中浮点数要求只保留两位小数。输出示例：
#a:hello,word; b:1.41; c:True; d:False; e:True
#定义一个字符串，使其输出结果如下图所示

def answer1():
    a = 'hello, world'
    b = 1.414
    c = (1 != 2)
    d = (True and False)
    e = (True or False)

    print("a:%s; b:%s c:%s d:%s e:%s" % (a, b, c, d, e))
    print("a:{}; b:{}; c{}; d{}; e{}".format(a, b, c, d, e))
def answer2():
    print("'%s'\n\\\"%s\""%('hello, word', 'hello, word'))
    print("'{0}'\n\\\"{0}\"".format("hello, world"))

if __name__ == '__main__':
    answer1()
    answer2()

