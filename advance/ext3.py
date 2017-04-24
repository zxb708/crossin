#【问题描述】
#BMI 指数（即身体质量指数，简称体质指数又称体重，英文为Body Mass Index，简称BMI），是用体重公斤数除以身高米数平方得出的数字
#BMI < 18.5 体重偏轻
#18.5 <= BMI < 24 体重正常
#BMI >= 24 体重偏重
#设计一个BMI计算器吧，看看自己体重是否正常。
#输入：身高、体重值
#输出：BMI 指数、是否正常


def get_bmi(weight, height):
    return weight / (height * height)

def display_info(weight, height):
    bmi = get_bmi(weight, height)

    print("The BMI is: %.2f" % bmi)
    if bmi < 18.5:
        print("体重偏轻")
    elif bmi < 24:
        print("体重正常")
    else:
        print("体重偏重")

if __name__ == '__main__':
    while True:
        try:
            weight = float(input("Please input your weight(kg):"))
            height = float(input("Please input your height(m):"))
            display_info(weight, height)
        except:
            print("Please input right data!")
            pass

        prompt = input("Do you want to continue(YES/NO):")
        while prompt.strip().lower() != "yes" and prompt.strip().lower() != "no":
            prompt = input("Do you want to continue(YES/NO):")
        if prompt.strip().lower() != "yes":
            print("Program will exit.\nHope you keep heath!")
            break