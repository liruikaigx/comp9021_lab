#Complete the program plane_encoding.py that implements a 
#function encode(a, b) and a function decode(n) for the one-to-one 
#mapping from the set of pairs of integers onto the set of natural 
#numbers, that can be graphically described as follows:

from math import sqrt


def encode(a, b):
    num_list = []
    for i in range(6):
        num_list.append([0]*6)
    x = 0
    y = 0
    temp = 1
    n = 0
    num_list[0][0] = 0
    while n<=1:
        for i in range(1, temp+1):
            num_list[x+i][y] = num_list[x][y]+i
        x = x+temp
        for j in range(1, temp+1):
            num_list[x][y+j] = num_list[x][y]+j
        y = y+temp
        for k in range(1, temp+2):
            num_list[x-k][y] = num_list[x][y]+k
        x = x-(temp+1)
        for l in range(1, temp+2):
            num_list[x][y-l] = num_list[x][y]+l
        y = y-(temp+1)
        temp = temp+2
        n += 1
    return num_list[a][b]
        
    
def decode(n):
    num_list = []
    for i in range(6):
        num_list.append([0]*6)
    x = 0
    y = 0
    temp = 1
    m = 0
    num_list[0][0] = 0
    if n == 0:
        return (0, 0)
    while m<=1:
        for i in range(1, temp+1):
            if num_list[x][y]+i == n:
                return (x+i, y)
            num_list[x+i][y] = num_list[x][y]+i
        x = x+temp
        for j in range(1, temp+1):
            if num_list[x][y]+j == n:
                return (x, y+j)
            num_list[x][y+j] = num_list[x][y]+j
        y = y+temp
        for k in range(1, temp+2):
            if num_list[x][y]+k == n:
                return (x-k, y)
            num_list[x-k][y] = num_list[x][y]+k
        x = x-(temp+1)
        for l in range(1, temp+2):
            if num_list[x][y]+l == n:
                return (x, y-l)
            num_list[x][y-l] = num_list[x][y]+l
        y = y-(temp+1)
        temp = temp+2
        m += 1
