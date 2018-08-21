# Finds all triples of consecutive positive three-digit integers
# each of which is the sum of two squares.

I = []
for i in range(0, 1000):
    I.append(None)
for a in range(32):
    for b in range(32):
        s = a*a + b*b
        if s < 1000:
            I[s] = (a, b)
for i in range(100, 998):
    if I[i] != None and I[i+1] != None and I[i+2] != None:
        a = I[i][0]
        b = I[i][1]
        c = I[i+1][0]
        d = I[i+1][1]
        e = I[i+2][0]
        f = I[i+2][1]
         
        print(f'({i}, {i + 1}, {i + 2}) (equal to ({b}^2+{a}^2, {d}^2+{c}^2, {f}^2+{e}^2)) is a solution.')