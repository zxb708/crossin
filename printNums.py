# -*- coding:utf-8 -*-


def printNums():
  for i in range(1, 5):
    for j in range(1, 5):
      for k in range(1, 5):
        if not( i == j == k):
          print("%d%d%d" % (i, j, k)
          
if __name__ == '__main__':
  printNums()
