'''
Prompts the user for a strictly positive integer, nb_of_elements,
generates a list of nb_of_elements random integers between 0 and 19, prints out the list,
computes the number of elements strictly less 5, 10, 15 and 20, and prints those out.
'''



from random import seed, randrange
import sys
try:
    arg_for_seed = int(input('Input a seed for the random number generator: '))
except ValueError:
    print('Input is not an integer, giving up.')
    sys.exit()   
try:
    nb_of_elements = int(input('How many elements do you want to generate? '))
except ValueError:
    print('Input is not an integer, giving up.')
    sys.exit()
if nb_of_elements <= 0:                                            #Check whether the input is strictly positive
    print('Input should be strictly positive, giving up.')
    sys.exit()

seed(arg_for_seed)
L = [randrange(20) for _ in range(nb_of_elements)]
print('\nThe list is:', L)
print()

quotient = [0] * 4
for i in range(nb_of_elements):
    quotient[L[i] // 5] += 1                        #Every element in L divided by 5
for i in range(4):                                  #find which range the element belongs to
    if quotient[i] == 0:
        print('There is no element', end = ' ')
    elif quotient[i] == 1:
        print('There is 1 element', end = ' ')
    else:
        print(f'There are {quotient[i]} elements', end = ' ')
    print(f'between {i*5} and {i*5+4}.')            #print the range
