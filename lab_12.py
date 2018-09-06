# Prompts the user for a number N and prints out the first N + 1 lines of Pascal triangle.

while True:
    try:
        N = int(input('Enter a nonnegative integer: '))
        if N < 0:
            raise ValueError
        break
    except ValueError:
        print('Incorrect input, try again')
num_list = []
for i in range(N+1):
    num_list.append([0]*(N+1))

for i in range(N+1):
    for j in range(i+1):
        if i == 0:
            num_list[i][j] = 1
        elif i == 1:
            num_list[i][j] = 1
        else:
            num_list[i][j] = num_list[i-1][j] + num_list[i-1][j-1]   #print the numbers in Pascal triangle

max_num = max(max(num_list))
digits = len(str(max_num))                              #the space number should be the length of digits of max_num
space = ' '
def print_space(n):                                     #This function used to print space
    for i in range(n):
        print(space, end="")

def print_number(num, n):                               #This function used to print print the number and add the space in front of number
    num_space = n - len(str(num))                       
    result = str(num)
    for i in range(num_space):
        result = space + result                    
    print(result, end="")
    
for i in range(N+1):
    print(space*(N-i)*digits, end="")                   #print the space first
    for j in range(i+1):
        if j == i:                                      
            print_number(num_list[i][j], digits)
        else:
            print_number(num_list[i][j], digits)
            print_space(digits)
    print()
