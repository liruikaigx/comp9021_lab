# Finds all sequences of consecutive prime 5-digit numbers,
# say (a, b, c, d, e, f), such that
# b = a + 2, c = b + 4, d = c + 6, e = d + 8, and f = e + 10.


def prime(number):# check whether the number is a prime or not 
 # using AKS algorithm 
 # integer -> bool 
    if number==2: 
        return True 
    if number==3: 
        return True 
    if number%2==0: 
        return False 
    if number%3==0: 
        return False 
    i=5 
    w=2 
    while i*i<=number: 
        if number%i==0: 
            return False 
        i+=w 
        w=6-w 
    return True
        
print('The solutions are:\n')
prime_list = []
for i in range(10000, 100000):
    if prime(i) == True:
        prime_list.append(i)
for j in range(len(prime_list)-5):
    if prime_list[j]+2 == prime_list[j+1] and prime_list[j+1]+4 == prime_list[j+2] and prime_list[j+2]+6 == prime_list[j+3] and prime_list[j+3]+8 == prime_list[j+4] and prime_list[j+4]+10 == prime_list[j+5]:
        print(f'{prime_list[j]} {prime_list[j+1]} {prime_list[j+2]} {prime_list[j+3]} {prime_list[j+4]} {prime_list[j+5]}')