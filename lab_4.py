'''
Prompts the user for a strictly positive integer, nb_of_elements,
generates a list of nb_of_elements random integers between -50 and 50, prints out the list,
computes the mean, the median and the standard deviation in two ways,
that is, using or not the functions from the statistics module, and prints them out.
'''


from random import seed, randint
from math import sqrt
from statistics import mean, median, pstdev
import sys

arg_for_seed = input('Input a seed for the random number generator: ')
try:
    arg_for_seed = int(arg_for_seed)
except ValueError:
    print('Input is not a integer, giving up.')
    sys.exit()
    
nb_of_elements = input('How many elements do you want to generate? ')
try:
    nb_of_elements = int(nb_of_elements)
except ValueError:
    print('Input is not a integer, giving up.')
    sys.exit()

if nb_of_elements <= 0:
    print('Input should be strictly positive, giving up.')
    sys.exit()


seed(arg_for_seed)
L = [randint(-50, 50) for _ in range(nb_of_elements)]
print('\nThe list is:', L)
print()

sort_L = sorted(L)                                 #sort the list

mean_s = 0
for e in L:
    mean_s = mean_s + e
mean_L = mean_s / nb_of_elements

if nb_of_elements % 2 == 1:                        #if nb_of_element is odd 
    median_L = float(sort_L[nb_of_elements//2])   
else:                                              #if nb_of_element is even
    median_L = float(sort_L[nb_of_elements//2] + sort_L[nb_of_elements//2-1])/2

pstdev_s = 0
for i in range(nb_of_elements):
    pstdev_s = pstdev_s + (sort_L[i] - mean_L) ** 2
pstdev_L = (pstdev_s / nb_of_elements) ** 0.5

print(f'The mean is {mean_L:0.2f}.')
print(f'The median is {median_L:0.2f}.')
print(f'The standard deviation is {pstdev_L:0.2f}.')
print('\nConfirming with functions from the statistics module:')
print(f'The mean is {mean(L):0.2f}.')
print(f'The median is {median(L):0.2f}.')
print(f'The standard deviation is {pstdev(L):0.2f}.')
