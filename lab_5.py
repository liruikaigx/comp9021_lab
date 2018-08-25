# Prompts the user to input an integer N at least equal to 10 and computes N!
# in three different ways.


import sys
from math import factorial

def first_computation(x):
    nb_of_trailing_0s = 0
    for i in range(len(str(x))):
        if x % (10 ** i) != 0:
            nb_of_trailing_0s = i-1
            break
    return nb_of_trailing_0s

def second_computation(x):
    i = -1
    str_f = str(x)
    while i <= 0:
        if int(str_f[i]) == 0:
            i = i - 1
        else:
            break
    return -i-1
    
def third_computation(x):
    nb_of_trailing_0s = 0
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
