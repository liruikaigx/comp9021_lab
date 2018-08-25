# Given a positive integer n, a magic square of order n is a matrix of size n x n
# that stores all numbers from 1 up to n^2 and such that the sum of the n rows,
# the sum of the n columns, and the sum of the two diagonals is constant,
# hence equal to n(n^2+1)/2.

def check1(square):
    for i in range(len(square)):
        if sum(square[i]) == (len(square)*(len(square)*len(square)+1))/2:
            return True
        else:
            return False

def check2(square):
    j_list = {}
    for i in range(len(square)):
        j_list[i] = []
    for a in range(len(square)):
        for b in range(len(square)):
            j_list[b].append(square[a][b])
    for m in j_list.values():
        if sum(m) != (len(square)*(len(square)*len(square)+1))/2:
            return False
            break
        else:
            return True
        
def check3(square):
    x_list = []
    y_list = []
    for a in range(len(square)):
        for b in range(len(square)):
            if a == b:
                x_list.append(square[a][b])
            elif a+b == len(square):
                y_list.append(square[a][b])
    
    if sum(x_list) == (len(square)*(len(square)*len(square)+1))/2 and sum(y_list) == (len(square)*(len(square)*len(square)+1))/2 or sum(y_list):
        return True
    else:
        return False
            
def is_magic_square(square):
    if check1(square) == True and check2(square) == True and check3(square) == True:
        return True
    else:
        return False
        
	
def print_square(square):
    for i in range(len(square)):
        for j in range(len(square)):
            if j == len(square)-1:
                print(square[i][j])
            else:
                print(f'{square[i][j]} ', end="")
