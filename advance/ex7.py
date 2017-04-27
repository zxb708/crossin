# -*- encoding:utf-8 -*-

def rect(width = 5, height = 5, symbol = '*'):
    #print the graph
    [print(symbol * width) for x in range(height)]


if __name__ == '__main__':
    rect()
    rect(4, 5)