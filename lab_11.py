# Prompts the user for a strictly positive number N
# and outputs an equilateral triangle of height N.
# The top of the triangle (line 1) is labeled with the letter A.
# For all nonzero p < N, line p+1 of the triangle is labeled
# with letters that go up in alphabetical order modulo 26
# from the beginning of the line to the middle of the line,
# starting wth the letter that comes next in alphabetical order
# modulo 26 to the letter in the middle of line p,
# and then down in alphabetical order modulo 26
# from the middle of the line to the end of the line.

while True:
    try:
        height = int(input('Enter strictly positive number: '))
        if height <= 0:
            raise ValueError
        break
    except ValueError:
        print('Incorrect input, try again.')

A_code = ord('A')
c = A_code

def print_space(n):
    for i in range(n):
        print(' ', end="")

def print_bletter(n):
    for i in range(n-1):
        if c+i <= 90:
            print(chr(c+i), end="")
        else:
            print(chr((c+i-65)%26 + 65), end="")   

def print_aletter(n):
    if n == 1:
        print()
    else:
        for i in range(n-1):
            if c+n-2-i <= 90:
                print(chr(c+n-2-i), end="")
            else:
                print(chr((c+n-2-i-65)%26 + 65), end="")
        print()
m = 0          
for i in range(1, height + 1):
    print_space(height-i)
    # Displays spaces on the left
    # Add your code here
    print_bletter(i)
    # Displays letters before middle column
    # Add your code here
    print(chr(m+A_code), end="")
    # Displays middle column
    # Add your code here
    print_aletter(i)
    # Displays letters after middle column
    # Add your code here

    # Code of first letter to be input on next line
    c = ((1 + i) * i // 2) % 26 + A_code
    m = (m+i+1)%26
