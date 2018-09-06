# Prompts the user to input an integer N at least equal to 10 and computes N!
# in three different ways.


import sys
from math import factorial

def first_computation(x):               #check whether this number can be devided by 10, 100, 1000,...,10**i?
    nb_of_trailing_0s = 0
    for i in range(len(str(x))):
        if x % (10 ** i) != 0:
            nb_of_trailing_0s = i-1
            break
    return nb_of_trailing_0s

def second_computation(x):              #transfer the integer into string and count the number of '0' in tail
    i = -1
    str_f = str(x)
    while i <= 0:
        if int(str_f[i]) == 0:
            i = i - 1
        else:
            break
    return -i-1
    
def third_computation(x):               #Every 10 can be divided into 2*5 and the times of 2 is greater than 5
    nb_of_trailing_0s = 0               #so the number of being divided by 10 can be transfered into divided by 5
    while x != 0:
        x //= 5
        nb_of_trailing_0s += x
    return nb_of_trailing_0s
    
try:
    the_input = int(input('Input a nonnegative integer: '))
    if the_input < 0:
        raise ValueError
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
    
the_input_factorial = factorial(the_input)
print(f'Computing the number of trailing 0s in {the_input}! by dividing by 10 for long enough:',
      first_computation(the_input_factorial))
print(f'Computing the number of trailing 0s in {the_input}! by converting it into a string:',
      second_computation(the_input_factorial))
print(f'Computing the number of trailing 0s in {the_input}! the smart way:',
      third_computation(the_input))
