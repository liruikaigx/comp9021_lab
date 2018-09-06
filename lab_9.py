# Finds all triples of positive integers (i, j, k) such that
# i, j and k are two digit numbers, i < j < k,
# every digit occurs at most once in i, j and k,
# and the product of i, j and k is a 6-digit number
# consisting precisely of the digits that occur in i, j and k.


for i in range(10, 100):
    for j in range(i+1, 100):
        for k in range(j+1, 100):
            prod = i * j * k
            str_i = str(i)
            str_j = str(j)
            str_k = str(k)
            str_prod = str(prod)
            L = [str_i[0], str_i[1], str_j[0], str_j[1], str_k[0], str_k[1]]#put all the numbers in i,j,k to L
            P = []
            for n in str_prod:
                P.append(n)                                                 #put all the numbers in prod to P
            if set(P) == set(L) and len(set(P)) == 6:                       #check
                print(f'{i} x {j} x {k} = {prod} is a solution.')
