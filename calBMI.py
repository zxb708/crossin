# -*- coding:utf-8 -*-

def calBMI(weight, height):
    bmi = weight / (height * height)
    return bmi



if __name__ == '__main__':
    weight = input("please enter your weight(unit:kg):")
    height = input("please enter your height(unit:m)")
    bmi = calBMI(float(weight), float(height))
    print(bmi)
    if bmi < 18.5:
        print("your weight is a little light. ")
    elif bmi >= 24:
        print("your are a little fat")
    else:
        print("your weight is normal")

