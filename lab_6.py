# Prompts the user for an integer N and finds all perfect numbers up to N.
# Quadratic complexity, can deal with small values only.


import sys

try:
    N = int(input('Input an integer: '))
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()

for i in range(2, N + 1):               
    sum1 = 0
    for s in range(1, i):         
        if i % s == 0:                #find the number which can divide i
            sum1 += s                 #sum them up and check
    if sum1 == i:
        print(f'{i} is a perfect number.')
