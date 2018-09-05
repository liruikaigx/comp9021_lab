# Prompts the user for a string w of lowercase letters and outputs the
# longest sequence of consecutive letters that occur in w,
# but with possibly other letters in between, starting as close
# as possible to the beginning of w.


import sys

letters = input('Please input a string of lowercase letters: ')

letter_list = []


for i in range(len(letters)):
    letter_list.append(set(letters[i]))
    temp = i
    for j in range(i+1, len(letters)):
        if ord(letters[j]) == ord(letters[temp]) + 1:
            letter_list[i].add(letters[j])
            temp = j

index = 0
for x in range(len(letter_list)-1):
    if len(letter_list[index]) < len(letter_list[x+1]):
        index = x+1

solution = ''
for y in sorted(letter_list[index]):
    solution = solution + y
    
print(f'The solution is: {solution}')