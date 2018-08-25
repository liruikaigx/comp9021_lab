# Decodes all multiplications of the form
#
#                        *  *  *
#                   x       *  *
#                     ----------
#                     *  *  *  *
#                     *  *  *
#                     ----------
#                     *  *  *  *
#
# such that the sum of all digits in all 4 columns is constant.

def sum_ith_digits(arr, i):
    s = 0
    for num in arr: 
        s = s + num // (10 ** i) % 10
    return s

def check1(num1, num2):
    prod1 = (num2 % 10) * num1
    prod2 = (num2 // 10) * num1
    prod = prod1 + prod2 * 10
    if prod1 >= 1000 and prod2 <= 1000:
        return True
    else:
        return False

def check2(num1,num2):
    prod1 = (num2 % 10) * num1
    prod2 = (num2 // 10) * num1 * 10
    prod = prod1 + prod2
    arr = [num1, num2, prod1, prod2, prod]
    A = sum_ith_digits(arr, 3)
    B = sum_ith_digits(arr, 2)
    C = sum_ith_digits(arr, 1)
    D = sum_ith_digits(arr, 0)
    if A == B and A == C and A == D:
        return True
    else:
        return False
    
for num1 in range(100, 1000):
    for num2 in range(10, 100):
        prod1 = (num2 % 10) * num1
        prod2 = (num2 // 10) * num1 * 10
        prod = prod1 + prod2
        arr = [num1, num2, prod1, prod2, prod]
        if check1(num1, num2) == True and check2(num1, num2) == True:
            print(f'{num1} * {num2} = {num1*num2}, all columns adding up to {sum_ith_digits(arr, 3)}.')
